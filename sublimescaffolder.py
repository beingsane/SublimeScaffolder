import sublime
import sublime_plugin


class SublimeScaffolderCommand(sublime_plugin.ApplicationCommand):
    def run(self, index):
        print "Not implemented but got argument: %s" % index


class CreateScaffold(object):

    def __run__(self):
        print "Creating scaffold..."

    def sayHello(self):
        return "hello"
