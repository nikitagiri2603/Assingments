import threading

def Thread1():
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Numbers from 1 to 50 :")
    for i in range(1, 51):
        print(i, end=" ")
    print()

def Thread2():
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Numbers from 50 to 1 :")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()


def main():
    print("Thread ID of main thread :", threading.get_ident())

    t1 = threading.Thread(target=Thread1, name="Thread1")
    t2 = threading.Thread(target=Thread2, name="Thread2")

    t1.start()
    t1.join()         

    t2.start()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()