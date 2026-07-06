def revsersedNumber(num):
    reversedNumber = 0
    while(num != 0):
        rem = num % 10
        reversedNumber = reversedNumber*10 + rem 
        num = num // 10  
    return reversedNumber

def main():
    value = int(input("Enter a number : "))
    reverse = revsersedNumber(value)
    print("The revserse of ",value," is ",reverse)

if __name__ == "__main__":
    main()