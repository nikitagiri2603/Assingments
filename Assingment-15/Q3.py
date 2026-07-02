Odd = lambda No:No%2!=0

def filterX(Task,Elements):
    Result = list()
    for i in Elements:
        Ret = Task(i)
        if(Ret == True):
            Result.append(i)
    return Result


def main():
    Data = list()
    n = int(input("Enter how many numbers you want in the list : "))
    for i in range(0,n):
        num = int(input())
        Data.append(num)

    print("Data is ",Data)
    FData = filterX(Odd,Data)
    print("Data after filter :",FData)

if __name__ == "__main__":
    main()