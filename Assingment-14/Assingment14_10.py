LargestofThree = lambda No1, No2, No3: No1 if No1 >= No2 and No1 >= No3 else (No2 if No2 >= No3 else No3)

def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))
    value3 = int(input("Enter third number : "))

    Ret = LargestofThree(value1, value2, value3)
    print("Largest is :", Ret)

if __name__ == "__main__":
    main()