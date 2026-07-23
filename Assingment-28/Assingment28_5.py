def searchWord(word,file):

    temp = ""
    Data = file.read()
    for ch in Data:
        if ch != " " and ch != "\n" and ch != "\t":
            temp = temp + ch
        else:
            if temp == word:
                return True
            temp = ""
    if temp == word:
        return True
    return False


def main():
    filename = input("Enter file name : ")
    str1 = input("Enter a word : ")

    try:
        fobj = open(filename, "r")
        
        ret = searchWord(str1,fobj)
        if ret == True:
            print("Word found in file")
        else:
            print("Word not found in file")

        fobj.close()

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()