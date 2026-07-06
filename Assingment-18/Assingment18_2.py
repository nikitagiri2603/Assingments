
def MaxinList(Elements):
    Max = Elements[0]
    for no in Elements:
        if(no > Max):
            Max = no
    return Max

def main():
    Data  = list()
    value = int(input("Enter number of elements in list :"))
    for i in range(0,value):
        no = int(input(f"Enter {i+1} element :"))
        Data.append(no)
    Max = MaxinList(Data)
    print("Maximum number in list is :",Max)

if __name__ == "__main__":
    main()