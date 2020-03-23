# NoteAutomator Winx64

### This is a compiled version of NoteAutomator for Windows Machines

### Compilation Details

- Compiled On: Windows 10 (x64) build 1903
- Executable compiled with [Pyinstaller Release: v3.6](https://github.com/pyinstaller/pyinstaller/releases/tag/v3.6)

> This redistributable is provided as it is, no warranties. The source code for this compilation points [here](https://github.com/KalleHallden/NoteAutomator/branches/all) 


If you do not like this redistributable, you can compile it yourself. Instructions for doing so, could be found on the [official manual](https://pythonhosted.org/PyInstaller/usage.html) from PyInstaller.


## How to use NoteAutomator

### Currently there are 3 commands for NoteAutomator

- `notes nfe NOTE_NAME FOLDER_NAME EXTENSION`

This option will open/create a note, NOTE_NAME.EXTENSION in a folder, FOLDER_NAME

- `notes on NOTE_NAME`

This option will find your note, NOTE_NAME, in all the folders. Extension not necessary while using this option

- `notes ne NOTE_NAME EXTENSION`

This option will open/create a note, NOTE_NAME.EXTENSION in the folder `General`

The name of the folder, variables, etc. can be modified, if you are building from source.



### Extra steps for Windows Users for a fully automated experience

- Create a folder named `src` in `C:/` drive. and save the `Notes.exe` executable in that folder
- Create an additional folder named `Notes` inside `src` folder for saving the notes.
 
> Optional : Add the `src` folder to your `Path` in System Environment Variables. This will let you call the notes from the terminal from anywhere.

### Optional: Adding src folder to path

[Windows-Commandline.com](https://www.windows-commandline.com/set-path-command-line/) has a great walkthrough for doing this quickly via the cmdline :)

- **TL;DR** paste this command in your [elevated command prompt](https://www.google.com/search?q=elevated+command+prompt&oq=elevated+command+prompt)

`setx path "%path%;c:\src"`

The above command only adds the path to your user account, so the other user accounts are safe from any changes.
Restart your command prompt and you should be able to automate your notes, right away.

Test if it is working:

`notes nfe HelloWorld MYFOLDER txt`


### List of Extensions

The NoteAutomator made by Kalle handles extensions quite well. It's versatile.
The complete usage is listed as below.


| __Extension__ | __Usage__ |
|-------------|-----------|
| Python      | `python`, `.py` |
| Text        | `text`, `.txt` |
| Java        |   `java`, `.java`|
| Dart/Flutter  |   `dart`, `.dart` |
| Yaml      | `yaml`, `.yaml` |
| Json      |   `json`, `.json`, `jason`    |
| Org       | `org`, `.org` |
| Markdown  | `markdown`, `.md` |
| PHP   |   `php`, `.php`   |
| Ruby   |   `ruby`, `.rb`   |
| JavaScript   |   `javascript`, `.js`, `js`   |
| TypeScript   |   `.ts`, `ts`   |
| XML   |   `xml`, `.xml`   |
| HTML   |   `html`, `.html`   |
| CSS   |   `css`, `.css`   |
