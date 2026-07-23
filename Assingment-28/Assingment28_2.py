def CountWords(file):
    count = 0
    inWord = False

    while True:
        ch = file.read(1)
        if ch == "":      
            break

        if ch != " " and ch != "\n" and ch != "\t":
            if inWord == False:
                count += 1
                inWord = True
        else:
            inWord = False

    return count


def main():
    filename = input("Enter file name : ")

    try:
        fobj = open(filename, "r")

        Ret = CountWords(fobj)

        print("Total number of words :", Ret)

        fobj.close()

    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()