def CountLines(file):
    count = 0

    while True:
        line = file.readline()

        if line == "":      
            break

        count += 1

    return count


def main():
    filename = input("Enter file name : ")

    try:
        fobj = open(filename, "r")

        Ret = CountLines(fobj)

        print("Total number of lines :", Ret)

        fobj.close()

    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()