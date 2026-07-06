
def SumOfDigits(No):
    Sum = 0

    while(No != 0):
        digit = No % 10
        Sum = Sum + digit
        No = No // 10

    return Sum

def main():
    value = int(input("Enter a number : "))
    Ret = SumOfDigits(value)

    print(f"Sum of digits in {value} is {Ret}")

if __name__ == "__main__":
    main()