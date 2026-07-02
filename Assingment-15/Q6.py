
Min = lambda No1, No2: No1 if No1 < No2 else No2

def reduceX(Task,Elements):
    Min = Elements[0]
    for no in Elements:
        Min = Task(Min,no)
    return Min

def main():
    Data = list()
    n = int(input("Enter how many numbers you want in the list : "))
    for i in range(0,n):
        num = int(input())
        Data.append(num)

    print("Data is ",Data)
    RData = reduceX(Min,Data)
    print("Data after reduce :",RData)

if __name__ == "__main__":
    main()

