SublimeScaffolder
=================


## What is sublime scaffolder?

It is a tool for you to quickly setup a project that you want to start on that usually have several files in common.
Like a webproject or something similar. With SublimeScaffolder you simply define the folders and files in your project 
that you know that you will use, if you want to download a file from the internet or copy the contents of a file on your harddrive 
you can do that aswell.

### How do I use SublimeScaffolder?

It's simple just press *ctrl+shift+k* followed by *ctrl+shift+s* and a menu with your defined scaffolds will show up, select
the one you want to run and press enter, after that you specify where you want it to be created.
When SublimeScaffolder is done setting up your scaffold it will create a new Sublime-project file for you which you can edit and save where you want.


### How do i configure SublimeScaffolder?

It's super easy, first you need to define a default folder in the settings Preferences -> Package Settings -> SublimeScaffolder -> Settings - User.
there you define the default_folder (This is just so that you dont have to type in the whole path all the time, which you could do if you want).
Then you define your scaffolds.

### Defining a scaffold:

Each scaffold has a name, so that you have something pretty and identifiable in the list of scaffolds.
And each scaffold has a contents object, within the contents objects you can define folders and files

#### FILES
A file looks like this:
<pre>
{'file':'filename.extension'}
</pre>

You can also specify if the file should have contents copied from somewhere on your harddrive like this:
<br/>
<pre>
{'file':'filename.extension', 'copy_from': "path_to_file_to_copy_contents_from"}
</pre>

Or if you want to download contents from the web and put in your file you do like this:
<pre>
{'file':'filename.extension', 'url': "url-to-file"}
</pre>

#### FOLDERS
Folders look pretty much like the whole scaffold, they have two attributes:
folder - which is the folder name
contents - what the folder should contain

So a folder could look something like this:
<pre>
{
    "folder":"src",
    "contents": [
        {'file':'filename.extension'}        
    ]
}
</pre>

#### Copying Directories(Folders)
Sometimes you might have a large setup, containing many default files and a default structure, in those cases the scaffolds might
become very large to write and thus errorprone, in those cases it might be better to copy a whole folder directly into your scaffold,
to do this use the *copydir* command:
<pre>
{
    "folder":"css",
    "contents": [
        {"copydir": "/home/username/default", "name":"awesomeness"}
    ]
}
</pre>
This will create a directory named *awesomeness" and put the contents from */home/username/default* into that directory.


If you get stuck you can always have a look in: Preferences -> Package Settings -> SublimeScaffolder -> Settings - Default where there is an example scaffold for you to use.



