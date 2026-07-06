Multiplication = lambda No1,No2: No1 * No2

def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))

    Ret = Multiplication(value1,value2)
    print("Multiplication is :",Ret)
   
if __name__ == "__main__":
    main()