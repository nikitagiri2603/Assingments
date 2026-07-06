def PrintSum(num):
    sum = 0
    for i in range(1,num+1):
        sum = sum + i
    print(sum)

def main():
    number = int(input("Enter value of n : "))
    PrintSum(number)

if __name__ == "__main__":
    main()