def DisplayFile(file):
    Data = file.read()
    print(Data)

def main():
    filename = input("Enter file name : ")

    try:
        fobj = open(filename, "r")

        DisplayFile(fobj)

        fobj.close()

    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()