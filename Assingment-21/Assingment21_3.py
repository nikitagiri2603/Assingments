import threading

Counter = 0
lock = threading.Lock()

def Increment():
    global Counter

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    for i in range(1, 101):
        lock.acquire()

        Counter = Counter + 1

        lock.release()


def main():
    global Counter

    print("Thread ID of main thread :", threading.get_ident())

    t1 = threading.Thread(target=Increment, name="Thread1")
    t2 = threading.Thread(target=Increment, name="Thread2")
    t3 = threading.Thread(target=Increment, name="Thread3")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Final value of Counter is :", Counter)

    print("Exit from main")


if __name__ == "__main__":
    main()