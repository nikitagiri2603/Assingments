import threading

def CheckPrime(No):
    if(No < 2):
        return False

    for i in range(2, No):
        if(No % i == 0):
            return False

    return True


def Prime(Data):
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    print("Prime numbers are :", end=" ")

    for no in Data:
        if(CheckPrime(no)):
            print(no, end=" ")

    print()


def NonPrime(Data):
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    print("Non Prime numbers are :", end=" ")

    for no in Data:
        if(CheckPrime(no) == False):
            print(no, end=" ")

    print()


def main():
    print("Thread ID of main thread :", threading.get_ident())

    Data = list()

    n = int(input("Enter how many numbers you want in the list : "))

    for i in range(0, n):
        num = int(input())
        Data.append(num)

    print("Data is :", Data)

    t1 = threading.Thread(target=Prime, args=(Data,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(Data,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()