def searchWord(word,file):

    temp = ""
    Data = file.read()
    count = 0
    for ch in Data:
        if ch != " " and ch != "\n" and ch != "\t":
            temp = temp + ch
        else:
            if temp == word:
                count = count + 1
            temp = ""
    if temp == word:
        count = count + 1
    return count


def main():
    filename = input("Enter file name : ")
    str1 = input("Enter a word : ")

    try:
        fobj = open(filename, "r")
        
        ret = searchWord(str1,fobj)

        print(f"The word is present in file {ret} times")
        fobj.close()

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()