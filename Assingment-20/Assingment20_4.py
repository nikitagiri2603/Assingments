import threading

def Small(str1):
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    Count = 0

    for ch in str1:
        if(ch >= 'a' and ch <= 'z'):
            Count = Count + 1

    print("Count of small letters is :", Count)


def Capital(str1):
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    Count = 0

    for ch in str1:
        if(ch >= 'A' and ch <= 'Z'):
            Count = Count + 1

    print("Count of capital letters is :", Count)


def Digits(str1):
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    Count = 0

    for ch in str1:
        if(ch >= '0' and ch <= '9'):
            Count = Count + 1

    print("Count of digits is :", Count)


def main():
    print("Thread ID of main thread :", threading.get_ident())

    str1 = input("Enter a string : ")

    t1 = threading.Thread(target=Small, args=(str1,), name="Small")
    t2 = threading.Thread(target=Capital, args=(str1,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(str1,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")


if __name__ == "__main__":
    main()