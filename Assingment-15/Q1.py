Square = lambda No:No*No

def mapX(Task,Elements):
    Result = list()
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    return Result

def main():
    Data = list()
    n = int(input("Enter how many numbers you want in the list : "))
    for i in range(0,n):
        num = int(input())
        Data.append(num)

    print("Data is ",Data)
    MData = mapX(Square,Data)
    print("Data after mapping :",MData)

if __name__ == "__main__":
    main()