
Add = lambda No1,No2:No1 + No2

def reduceX(Task,Elements):
    Sum = 0
    for no in Elements:
        Sum  = Task(Sum,no)
    return Sum

def main():
    Data = list()
    n = int(input("Enter how many numbers you want in the list : "))
    for i in range(0,n):
        num = int(input())
        Data.append(num)

    print("Data is ",Data)
    RData = reduceX(Add,Data)
    print("Data after reduce :",RData)

if __name__ == "__main__":
    main()