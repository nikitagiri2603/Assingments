
def positiveNegativZero(No):
    if(No > 0):
        print(f"{No} is positive number")
    elif(No==0):
        print(f"{No} is zero")
    else:
        print(f"{No} is negative number")

def main():
    value = int(input("Enter a number :"))
    positiveNegativZero(value)

if __name__ == "__main__":
    main()
