import multiprocessing
import os
import time

def SumPower(no):
    Sum = 0

    for i in range(1, no + 1):
        Sum = Sum + (i ** 5)

    print("Process ID:", os.getpid(), " N:", no)
    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    Start = time.time()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumPower, Data)

    pobj.close()
    pobj.join()

    End = time.time()

    print("\nResults:")
    for no, ans in zip(Data, Result):
        print("N =", no, " Sum =", ans)

    print("\nTotal Execution Time:", End - Start, "seconds")

if __name__ == "__main__":
    main()