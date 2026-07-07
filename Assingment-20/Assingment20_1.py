import time
import threading

def Even():
    print("TID of Even thread is", threading.get_ident())
    for i in range(1, 11):
        print(i * 2, end=" ")
    print()


def Odd():
    print("TID of Odd thread is", threading.get_ident())
    for i in range(1, 11):
        print((i * 2) - 1, end=" ")
    print()

def main():
    print("TID of main thread is", threading.get_ident())

    start_time = time.perf_counter()

    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"Time required is {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()