import threading

def EvenList(Data):
    print("TID of EvenList thread is", threading.get_ident())

    Sum = 0

    print("Even elements are :", end=" ")

    for no in Data:
        if(no % 2 == 0):
            print(no, end=" ")
            Sum = Sum + no

    print("\nSum of Even elements is :", Sum)


def OddList(Data):
    print("TID of OddList thread is", threading.get_ident())

    Sum = 0

    print("Odd elements are :", end=" ")

    for no in Data:
        if(no % 2 != 0):
            print(no, end=" ")
            Sum = Sum + no

    print("\nSum of Odd elements is :", Sum)


def main():
    print("TID of main thread is", threading.get_ident())

    Data = list()

    n = int(input("Enter how many elements you want in the list : "))

    for i in range(0, n):
        num = int(input())
        Data.append(num)

    print("Data is :", Data)

    t1 = threading.Thread(target=EvenList, args=(Data,))
    t2 = threading.Thread(target=OddList, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()