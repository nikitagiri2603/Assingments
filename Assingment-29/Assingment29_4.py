
import sys
def CompareContents(file1,file2):
    try:
        fobj1 = open(file1,"r")
        fobj2 = open(file2,"r")
        if(fobj1.read() == fobj2.read()):
            print("Success")
        else:
            print("Failure")
        fobj1.close()
        fobj2.close()
    except Exception as eobj:
        print("Error occured")

def main():

    if(len(sys.argv) == 3):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This program is used to copy one file content into another")
            print("For better usage please check --u flag")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the file as ")
            print("python FileName.py TextfileName")
        else:
            CompareContents(sys.argv[1],sys.argv[2])
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

if __name__ == "__main__":
    main()