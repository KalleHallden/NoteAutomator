
import sys
import os 

python = ".py"
java = ".java"
dart = ".dart"
text = ".txt"

extensions = {
    "python" : python,
    ".py" : python,
    "text" : text,
    ".txt" : text,
    "java" : java,
    ".java" : java,
    "dart" : dart,
    "flutter" : dart,
    ".dart" : dart
}

def create():
    extension = str(sys.argv[3])
    folderName = str(sys.argv[2])
    fileName = str(sys.argv[1])
    os.chdir("./Notes")
    try:
        extension = extensions[extension]
    except Exception:
        extension = ".txt"

    fileName = fileName + extension
    if os.path.isdir("./" + folderName):
        os.chdir("./" + folderName)
    else:
        os.mkdir(folderName)
        os.chdir("./" + folderName)
    
    if not os.path.isfile("./" + fileName):
        open(fileName, "a").close()

    os.system("subl " + fileName)

if __name__ == "__main__":
    create()






























