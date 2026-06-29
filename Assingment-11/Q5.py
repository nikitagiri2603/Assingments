def ChkPalindrome(num):
    temp = num
    reversedNumber = 0
    while(num != 0):
        rem = num % 10
        reversedNumber = reversedNumber*10 + rem 
        num = num // 10  
    if(reversedNumber == temp):
        return True
    else:
        return False

def main():
    value = int(input("Enter a number : "))
    checknumber = ChkPalindrome(value)
    if(checknumber == True):
        print("The number is Palindrome")
    else:
        print("The number is not palindrome")

if __name__ == "__main__":
    main()