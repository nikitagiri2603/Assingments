
Odd = lambda No: True if No%2!=0 else False

def main():
    value1 = int(input("Enter first number : "))
    Ret = Odd(value1)
    if(Ret):
        print("Number is Odd")
    else:
        print("Number is Even")
        
if __name__ == "__main__":
    main()