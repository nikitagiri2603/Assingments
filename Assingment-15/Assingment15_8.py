
divisibleby3and5 = lambda No: No%3==0 and No%5 == 0

def filterX(Task,Elements):
    Result = list()
    for no in Elements:
        Ret = Task(no)
        if(Ret == True):
            Result.append(no)
    return Result

def main():
    Data = list()
    n = int(input("Enter how many numbers you want in the list : "))
    for i in range(0,n):
        num = int(input())
        Data.append(num)

    print("Data is ",Data)
    FData = filterX(divisibleby3and5,Data)
    print("Data after reduce :",FData)

if __name__ == "__main__":
    main()

