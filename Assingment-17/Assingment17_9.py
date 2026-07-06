
def countDigits(No):
    count = 0
    while(No != 0):
        count = count + 1
        No = No // 10
    return count

def main():
    value = int(input("Enter a number : "))
    Ret = countDigits(value)

    print(f"No. of digits in {value} is {Ret}")

if __name__ == "__main__":
    main()