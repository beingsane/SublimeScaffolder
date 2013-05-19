import sublime
import sublime_plugin
import os
import urllib2
import threading

class SublimeScaffoldMenuCommand(sublime_plugin.WindowCommand):

    def __init__(self, window):
        self.win = window

    def run(self):
        sets = sublime.load_settings("SublimeScaffolder.sublime-settings")
        self.scaffolds = sets.get("scaffolds")
        self.project_root = sets.get("default_folder", "")

        if self.project_root == "":
            sublime.status_message("No default folder defined!")
            return
        if self.scaffolds is None:
            sublime.status_message("No scaffolds defined!")
            return
        
        self.win.show_quick_panel(self.get_scaffolds(), self.select_path)

    def get_scaffolds(self):
        return [scaffold["name"] for scaffold in self.scaffolds]

    def select_path(self, idx):
        if idx == -1:
            sublime.status_message("Cancelled scaffolding.")
            return
        
        self.selected_scaffold = self.scaffolds[idx]
        self.win.show_input_panel("Where should i create the scaffold?", self.project_root, self.create_scaffold, None, self.on_cancel)

    def on_cancel(self):
        sublime.status_message("Cancelled scaffolding.")
        self.selected_index = None

    def create_scaffold(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            contents = "Path \"%s\" already exists, please choose another location!" % path
            self.win.run_command("scaffolding_result", {"contents":contents})
            return

        sublime.status_message("Creating scaffold.")
        creator_thread = ScaffoldCreator(self.selected_scaffold, path)
        creator_thread.start()
        while creator_thread.is_alive():
            continue
        contents = "{\n\t\"folders\":\n\t[\n\t\t{\n\t\t\t\"path\":\"%s\"\n\t\t}\n\t]\n}" % path
        self.win.run_command("scaffolding_result", {"contents":contents})


class ScaffoldingResultCommand(sublime_plugin.TextCommand):
    def run(self, edit, contents):
        project_file = self.view.window().new_file()
        project_file.insert(edit, 0, contents)
        self.window.active_view(project_file)


class ScaffoldCreator(threading.Thread):

    def __init__(self, scaffold, root_path):
        self.scaffold = scaffold
        self.root_path = root_path
        self.done = False
        threading.Thread.__init__(self)

    def run(self):
        self.create_recursively(self.scaffold["contents"], self.root_path)
        self.done = True

    def create_recursively(self, contents, path):
        for item in contents:
            if "file" in item:
                self.create_file_item(item, path)
            elif "folder" in item:
                new_path = "%s/%s" % (path, item["folder"])
                os.makedirs(new_path)
                self.create_recursively(item["contents"], new_path)

    def create_file_item(self, item, path):
        file_path = "%s/%s" % (path, item["file"])
        new_file = open(file_path, 'a+')

        if "url" in item:
            contents = urllib2.urlopen(item['url']).read()
            new_file.write(contents)
        if "copy_from" in item:
            copy_file = open(item["copy_from"], "r")
            new_file.write(copy_file.read())
            copy_file.close()
        new_file.close()
