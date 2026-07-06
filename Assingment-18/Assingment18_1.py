
def AdditionList(Elements):
    Sum = 0
    for no in Elements:
        Sum = Sum + no
    return Sum

def main():
    Data  = list()
    value = int(input("Enter number of elements in list :"))
    for i in range(0,value):
        no = int(input(f"Enter {i+1} element :"))
        Data.append(no)

    print(Data)
    Ret = AdditionList(Data)
    print("Addition of elements in list is :",Ret)

if __name__ == "__main__":
    main()