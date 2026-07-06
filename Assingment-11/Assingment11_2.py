def countDigits(num):
    if num == 0:
        return 1
    cnt = 0
    while(num != 0):
        rem = num % 10
        num = num // 10
        cnt = cnt + 1 
    return cnt

def main():
    value = int(input("Enter a number : "))
    count = countDigits(value)
    print("The number of digits in ",value," is ",count)


if __name__ == "__main__":
    main()