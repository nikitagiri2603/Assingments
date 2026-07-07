import threading

Sum = 0
Product = 1

def SumList(Data):
    global Sum

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    for no in Data:
        Sum = Sum + no


def ProductList(Data):
    global Product

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    for no in Data:
        Product = Product * no


def main():
    global Sum
    global Product

    print("Thread ID of main thread :", threading.get_ident())

    Data = list()

    n = int(input("Enter how many numbers you want in the list : "))

    for i in range(0, n):
        num = int(input())
        Data.append(num)

    print("Data is :", Data)

    t1 = threading.Thread(target=SumList, args=(Data,), name="SumThread")
    t2 = threading.Thread(target=ProductList, args=(Data,), name="ProductThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements is :", Sum)
    print("Product of elements is :", Product)

    print("Exit from main")


if __name__ == "__main__":
    main()