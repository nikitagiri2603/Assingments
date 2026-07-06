
def ChkPrime(Num):
    cnt = 0
    for i in range(1,Num+1):
        if(Num % i == 0):
            cnt = cnt + 1
    return cnt

def main():
    value = int(input('Enter a number :'))
    Ret = ChkPrime(value)
    if(Ret == 2):
        print(f"{value} is Prime")
    else:
        print(f"{value} is NOT Prime")

if __name__ == "__main__":
    main()