import multiprocessing
import os

def Factorial(no):
    fact = 1

    for i in range(1, no + 1):
        fact = fact * i

    print("Process ID :", os.getpid())
    print("Input Number :", no)
    print("Factorial :", fact)
    print()

    return fact

def main():
    Data = [10, 15, 20, 25]

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial, Data)

    pobj.close()
    pobj.join()

    print("Final Result:")
    print(Result)

if __name__ == "__main__":
    main()