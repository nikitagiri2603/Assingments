
chkEven = lambda No : No%2==0

Square = lambda No : No*No

Addition = lambda No1,No2: No1+No2

def filterX(Task,Elements):
    Result = list()
    for no in Elements:
        Ret = Task(no)
        if(Ret):
            Result.append(no)
    return Result

def mapX(Task,Elements):
    Result = list()
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    return Result
    

def reduceX(Task,Elements):
    Result = 0
    for no in Elements:
        Result = Task(Result,no)
    return Result


def main():
    Data  = list()
    value = int(input("Enter number of elements in list :"))
    for i in range(0,value):
        no = int(input(f"Enter {i+1} element :"))
        Data.append(no)

    FData = filterX(chkEven,Data)
    print("Data after filter :",FData)

    MData = mapX(Square,FData)
    print("Data after map :",MData)

    RData = reduceX(Addition,MData)
    print("Data after reduce :",RData)

if __name__ == "__main__":
    main()
