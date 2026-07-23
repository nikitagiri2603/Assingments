def DisplayContent(file):
    Data = file.read()
    print(Data)

def main():
    try:
        fileName = input("Enter file name :")
        fobj = open(fileName,"r")
        DisplayContent(fobj)
        fobj.close()
    except FileNotFoundError as fobj:
        print("File not found")
if __name__ == "__main__":
    main()