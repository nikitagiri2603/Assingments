def CopyContent(source,destination):
    Data = source.read()
    destination.write(Data)

def main():
    try:

        SourceFile = input("Enter existing file name : ")
        DestinationFile = input("Enter new file name : ")

        source = open(SourceFile,"r")
        destination = open(DestinationFile,"w")
        
        CopyContent(source,destination)


        print("Contents copied successfully")

        source.close()
        destination.close()

    except FileNotFoundError:
        print("Source file not found")

if __name__ == "__main__":
    main()