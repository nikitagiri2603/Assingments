
product = lambda No1,No2 : No1 * No2

def reduceX(Task,Elements):
    Product = 1
    for no in Elements:
        Product = Task(Product,no)
    return Product

def main():
    Data = list()
    n = int(input("Enter how many numbers you want in the list : "))
    for i in range(0,n):
        num = int(input())
        Data.append(num)

    print("Data is ",Data)
    FData = reduceX(product,Data)
    print("Data after reduce :",FData)

if __name__ == "__main__":
    main()

