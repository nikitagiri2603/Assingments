def ChkVowelorConsonant(s):
    if(s.lower() == ('a' or 'e' or 'i' or 'o' or 'u')):
        print(s, "is vowel " )
    else:
        print(s, "is consonant")
def main():
    string = input("Enter a number : ")
    ChkVowelorConsonant(string)

if __name__ == "__main__":
    main()