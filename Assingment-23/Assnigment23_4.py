import multiprocessing
import os

def CountOdd(no):
    Count = 0

    for i in range(1, no + 1, 2):
        Count = Count + 1

    print("Process ID :", os.getpid())
    print("Input Number :", no)
    print("Odd Number Count :", Count)
    print()

    return Count

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(CountOdd, Data)

    pobj.close()
    pobj.join()

    print("Final Result:")
    print(Result)

if __name__ == "__main__":
    main()