
def CheckPrime(No):
    if(No < 2):
        return False
    for i in range(2, No):
        if(No % i == 0):
            return False
    return True

MultiplyBy2 = lambda No : No * 2

Maximum = lambda No1, No2 : No1 if No1 > No2 else No2

def filterX(Task, Elements):
    Result = list()
    for no in Elements:
        Ret = Task(no)
        if(Ret == True):
            Result.append(no)
    return Result

def mapX(Task, Elements):
    Result = list()
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    return Result

def reduceX(Task, Elements):
    Max = Elements[0]
    for no in Elements[1:]:
        Max = Task(Max, no)
    return Max


def main():
    Data  = list()
    value = int(input("Enter number of elements in list :"))
    for i in range(0,value):
        no = int(input(f"Enter {i+1} element :"))
        Data.append(no)

    print("Input List :", Data)

    FData = filterX(CheckPrime, Data)
    print("List after filter :", FData)

    MData = mapX(MultiplyBy2, FData)
    print("List after map :", MData)

    RData = reduceX(Maximum, MData)
    print("Data after reduce :", RData)

if __name__ == "__main__":
    main()