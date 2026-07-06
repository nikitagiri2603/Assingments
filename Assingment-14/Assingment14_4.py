
Max = lambda No1, No2: No1 if No1 < No2 else No2

def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))
    Ret = Max(value1,value2)
    print("Minimum of number is :",Ret)

if __name__ == "__main__":
    main()