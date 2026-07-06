def additionofFactors(no):
    Sum = 0
    for i in range(1, no):
        if(no % i == 0):
            Sum = Sum + i
    return Sum
def main():
    value = int(input("Enter a number : "))
    Ret = additionofFactors(value)

    print(f"Addition of factors of {value} is {Ret}")

if __name__ == "__main__":
    main()