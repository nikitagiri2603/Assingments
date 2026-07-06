
def countlengthofstring(str1):
    count = 0
    for ch in str1:
        count = count + 1
    return count

def main():
    string = input("Enter a string :")
    Ret = countlengthofstring(string)
    print(f"The length of {string} is {Ret}")

if __name__ == "__main__":
    main()