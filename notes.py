
import sys
import os 

def create():
    print(sys.argv)
    fileName = str(sys.argv[1]) + str(sys.argv[3])
    open(fileName, "a").close()
    os.system("subl " + fileName)

if __name__ == "__main__":
    create()






























