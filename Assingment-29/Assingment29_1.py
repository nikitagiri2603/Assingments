import os
def main():
    try:
        fileName = input("Enter file name :")
        ret = os.path.exists(fileName)
        if ret == True:
            print("File is present in current directory")
        else:
            print("There is no such file")
            
    except FileNotFoundError as fobj:
        print("File not found in current directory")

if __name__ == "__main__":
    main()