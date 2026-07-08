

import time
import threading

def Even(No):
    print("Even numbers are :")
    for i in range(0,11):
        if(i%2==0):
            print(i,end=" ")
    print()
 
def Odd(No):
    print("Odd numbers are :")
    for i in range(0,11):
        if(i%2!=0):
            print(i,end=" ")

def main():

    start_time = time.perf_counter()
    t1 = threading.Thread(target=Even,args=(11,))
    t2 = threading.Thread(target=Odd,args=(11,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.perf_counter()
    print()
    print(f"Time required is {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()