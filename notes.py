#!/bin/python3.7


import sys
import os 


class NoteAutomator: 
    ruby = ".rb"
    php = ".php"
    javascript = ".js"
    typescript = ".ts"
    python = ".py"
    java = ".java"
    csharp = ".cs"
    dart = ".dart"
    text = ".txt"
    yaml = ".yaml"
    xml = ".xml"
    html = ".html"
    css = ".css"
    json = ".json"
    org = ".org"
    markdown = ".md"

    extensions = {
        "python" : python,
        ".py" : python,
        "text" : text,
        ".txt" : text,
        "java" : java,
        ".java" : java,
        "dart" : dart,
        "flutter" : dart,
        ".dart" : dart,
        "yaml" : yaml,
        ".yaml" : yaml,
        "json" : json,
        "jason" : json,
        ".json" : json,
        "org" : org,
        ".org" : org,
        "markdown" : markdown,
        ".md" : markdown,
        "php" : php,
        ".php" : php,
        "ruby" : ruby,
        ".rb" : ruby,
        "javascript" : javascript,
        "js" : javascript,
        ".js" : javascript,
        "ts" : typescript,
        "xml" : xml,
        ".xml" : xml,
        "html" : html,
        ".html": html,
        "css" : css,
        ".css" : css
    }

    extension = ""
    folderName = ""
    fileName = ""
    foundFileExtension = ""
    path = os.getcwd()

    def getArgs(self, ext_num, fold_num):
        try:
            self.extension = str(sys.argv[ext_num]).lower()
            self.extension = self.extensions[self.extension]
        except Exception:
            self.extension = ".txt"
        try:
            self.folderName = str(sys.argv[fold_num])
        except Exception:
            self.folderName = "General"
        try:
            self.fileName = str(sys.argv[2])
        except Exception:
            print("Name your note")
            sys.exit()

    def createNoteAndFolder(self):
        os.chdir("./Notes")

        self.fileName = self.fileName + self.extension
        if not os.path.isdir("./" + self.folderName):
            os.mkdir(self.folderName)
            
        os.chdir("./" + self.folderName)
    
        if not os.path.isfile("./" + self.fileName):
            open(self.fileName, "a").close()

        os.system("subl " + self.fileName)
    
    def findFileInFolder(self, folder):
        if os.path.isdir(self.path + "/" + folder):
            self.path = self.path + "/" + folder
            self.findFile(self.fileName, "", self.path)
        else:
            self.path = self.findFolder(folder, "", self.path)
            self.findFile(self.fileName, "",  self.path)
        
        # print(self.path)
        os.system("subl " + self.path)
    
    def findFile(self, fileToFind, folderToSearch, thepath):
        fileExists = False
        pathToFolder = ""
        for subdir, dirs, files in os.walk(thepath + folderToSearch):
            for dir_ in dirs:
                if dir_.lower() == self.folderName.lower():
                    pathToFolder = ""
                    pathToFolder = subdir + "/" + self.folderName
            for file_ in files:
                name = ""
                for i in range(len(str(file_))):
                    if len(str(self.fileName)) > i:
                        if str(file_).lower()[i] == str(self.fileName).lower()[i]:
                            name = name + str(file_)[i]
                            if len(name) > len(self.fileName) * 0.8:
                                self.path = os.path.join(subdir, file_)
                                fileExists = True
                                break
        if not fileExists:
            self.path = os.path.join(pathToFolder ,self.fileName + self.extension)
            open(self.path, "a").close()



if __name__ == "__main__":
    notes = NoteAutomator()

    command = str(sys.argv[1])

    if command == "nfe":
        notes.getArgs(4, 3)
        notes.createNoteAndFolder()
    if command == "on":
        notes.getArgs(4, 3)
        try: 
            notes.findFileInFolder(str(sys.argv[3]))
        except Exception:
            notes.findFileInFolder("")
    if command == "ne":
        notes.getArgs(3, 10)
        notes.findFileInFolder("")
        

