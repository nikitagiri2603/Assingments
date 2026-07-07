import threading

def EvenFactor(No):
    print("TID of EvenFactor thread is", threading.get_ident())

    Sum = 0

    print("Even Factors are :", end=" ")

    for i in range(1, No + 1):
        if(No % i == 0):
            if(i % 2 == 0):
                print(i, end=" ")
                Sum = Sum + i

    print("\nSum of Even Factors is :", Sum)


def OddFactor(No):
    print("TID of OddFactor thread is", threading.get_ident())

    Sum = 0

    print("Odd Factors are :", end=" ")

    for i in range(1, No + 1):
        if(No % i == 0):
            if(i % 2 != 0):
                print(i, end=" ")
                Sum = Sum + i

    print("\nSum of Odd Factors is :", Sum)


def main():
    print("TID of main thread is", threading.get_ident())

    value = int(input("Enter a number : "))

    t1 = threading.Thread(target=EvenFactor, args=(value,))
    t2 = threading.Thread(target=OddFactor, args=(value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()