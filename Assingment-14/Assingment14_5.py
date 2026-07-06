
Even = lambda No: True if No%2==0 else False

def main():
    value1 = int(input("Enter first number : "))
    Ret = Even(value1)
    if(Ret):
        print("Number is Even")
    else:
        print("Number is Odd")
        
if __name__ == "__main__":
    main()