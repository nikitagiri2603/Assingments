import multiprocessing
import os 
import time

def Squares(No):
    print("Process is Running with PID",os.getpid())
    Sum = 0
    for i in range(1,No+1):
        Sum = Sum + (i**2)
    return Sum 

def main():

    Data = []
    Result = []
    print("Enter how many numbers you want in the list :")
    n = int(input())
    for i in range(1,n+1):
        print("Element ",i," :")
        no = int(input())
        Data.append(no)

    start_time = time.perf_counter()
    pobj = multiprocessing.Pool()              
    Result = pobj.map(Squares,Data)            
    pobj.close()
    pobj.join()
    end_time = time.perf_counter()

    print("Result is :")
    print(Result)
    print(f"Time required is : {end_time - start_time:.4f} seconds")
    
if __name__ == "__main__":
    main()
