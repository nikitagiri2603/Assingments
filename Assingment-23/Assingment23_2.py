import multiprocessing
import os

def SumOdd(no):
    Sum = 0

    for i in range(1, no + 1, 2):
        Sum = Sum + i

    print("Process ID :", os.getpid())
    print("Input Number :", no)
    print("Sum of Odd Numbers :", Sum)
    print()

    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOdd, Data)

    pobj.close()
    pobj.join()

    print("Final Result:")
    print(Result)

if __name__ == "__main__":
    main()