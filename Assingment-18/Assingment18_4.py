
def countFrequency(no,Elements):
    count = 0
    for i in Elements:
        if(i == no):
            count = count+1
    return count

def main():
    Data  = list()
    value = int(input("Enter number of elements in list :"))
    for i in range(0,value):
        no = int(input(f"Enter {i+1} element :"))
        Data.append(no)
    no = int(input("Enter a number to check in list :"))
    Ret = countFrequency(no,Data)
    print(f"Frequency of {no} in {Data} is {Ret}")

if __name__ == "__main__":
    main()