
def MininList(Elements):
    Min = Elements[0]
    for no in Elements:
        if(no < Min):
            Min = no
    return Min

def main():
    Data  = list()
    value = int(input("Enter number of elements in list :"))
    for i in range(0,value):
        no = int(input(f"Enter {i+1} element :"))
        Data.append(no)
    Min = MininList(Data)
    print("Minimum number in list is :",Min)

if __name__ == "__main__":
    main()