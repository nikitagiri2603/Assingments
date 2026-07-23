import sys

def CopyContents(file1):
    try:
        fobj = open("Demo.txt","w")
        fb = open(file1,"r")
        Data = fb.read()
        fobj.write(Data)
        fobj.close()
        fb.close()
        print("Data copied successfully")
    except Exception as eobj:
        print("Error occured")

def main():

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This program is used to copy one file content into another")
            print("For better usage please check --u flag")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the file as ")
            print("python FileName.py TextfileName")
        else:
            CopyContents(sys.argv[1])
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

if __name__ == "__main__":
    main()