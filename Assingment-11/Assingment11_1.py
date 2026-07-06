def PrimeNumber(num):
    cnt = 0
    for i in range(1,num+1):
        if(num % i == 0):
            cnt = cnt + 1

    if(cnt == 2):
        return True
    else:
        return False


def main():
    value = int(input("Enter a number : "))
    ans = PrimeNumber(value)
    if(ans == True):
        print(value ,"is Prime")
    else:
        print(value ,"is Not Prime")


if __name__ == "__main__":
    main()