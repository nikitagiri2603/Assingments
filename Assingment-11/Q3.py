def sumofDigits(num):
    sum =0
    while(num != 0):
        rem = num % 10
        num = num // 10
        sum = sum + rem
    return sum

def main():
    value = int(input("Enter a number : "))
    sum = sumofDigits(value)
    print("The sum of digits in ",value," is ",sum)


if __name__ == "__main__":
    main()