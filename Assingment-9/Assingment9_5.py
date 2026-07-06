def chkDivisibility(num):
    if(num%3==0 and num%5==0):
        print("Yes the number is divisible by 3 and 5")
    else:
        print("No the number is not divisible by 3 and 5")

def main():
    value = int(input("Enter a number : "))
    chkDivisibility(value)

if __name__ == "__main__":
    main()
