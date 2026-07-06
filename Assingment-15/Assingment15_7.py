
lengthGreaterthan5 = lambda str1 : len(str1) > 5

def filterX(Task,Elements):
    Result = list()
    for str1 in Elements:
        Ret = Task(str1)
        if(Ret == True):
            Result.append(str1)
    return Result

def main():
    Data = list()
    n = int(input("Enter how many words you want in the list : "))
    for i in range(0,n):
        str1 = input()
        Data.append(str1)

    print("Data is ",Data)
    FData = filterX(lengthGreaterthan5,Data)
    print("Data after reduce :",FData)

if __name__ == "__main__":
    main()

