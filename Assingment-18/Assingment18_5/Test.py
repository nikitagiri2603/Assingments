import MarvellousNum

def ListPrime(Elements):
    Sum = 0

    for i in Elements:
        if(MarvellousNum.ChkPrime(i)):
            Sum = Sum + i

    return Sum

def main():
    Data = list()

    value = int(input("Enter number of elements : "))

    for i in range(value):
        no = int(input(f"Enter {i+1} element : "))
        Data.append(no)

    Ret = ListPrime(Data)

    print(f"Addition of prime numbers is {Ret}")

if __name__ == "__main__":
    main()