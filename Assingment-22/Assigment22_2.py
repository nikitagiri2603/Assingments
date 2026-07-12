import os
import multiprocessing

def Factorial(no):
    fact = 1
    for i in range(1, no + 1):
        fact = fact * i
    
    print("Process ID:", os.getpid(), " Input:", no, " Factorial:", fact)
    return fact

def main():
    Data = []
    
    print("Enter how many numbers you want in the list:")
    n = int(input())
    
    for i in range(1, n + 1):
        print("Element", i, ":")
        no = int(input())
        Data.append(no)
    
    print("Input List:", Data)

    pobj = multiprocessing.Pool()
    Result = pobj.map(Factorial, Data)
    
    pobj.close()
    pobj.join()

    print("\nFinal Result List:")
    print(Result)

if __name__ == "__main__":
    main()