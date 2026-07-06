
def ChkDivisibeby5(No):
    return No % 5 == 0

def main():
    value = int(input("Enter a number :"))
    Ret = ChkDivisibeby5(value)
    if(Ret):
        print(f"{value} is divisible by 5")
    else:
        print(f"{value} is NOT divisible by 5")


if __name__ == "__main__":
    main()