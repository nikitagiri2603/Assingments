import threading

def Maximum(Data):
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    Max = Data[0]

    for no in Data:
        if(no > Max):
            Max = no

    print("Maximum element is :", Max)


def Minimum(Data):
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    Min = Data[0]

    for no in Data:
        if(no < Min):
            Min = no

    print("Minimum element is :", Min)


def main():
    print("Thread ID of main thread :", threading.get_ident())

    Data = list()

    n = int(input("Enter how many numbers you want in the list : "))

    for i in range(0, n):
        num = int(input())
        Data.append(num)

    print("Data is :", Data)

    t1 = threading.Thread(target=Maximum, args=(Data,), name="Maximum")
    t2 = threading.Thread(target=Minimum, args=(Data,), name="Minimum")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()