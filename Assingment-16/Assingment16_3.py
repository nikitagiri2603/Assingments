
def Add(No1,No2):
    Ans = No1 + No2
    return Ans

def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))

    Ret = Add(value1,value2)

    print(f"Addition is {Ret}")

if __name__ == "__main__":
    main()