
import threading
import time

def DisplayEven(No):
    SumEvenFactors = 0
    for i in range(1,No+1):
        if(No%i==0 and i%2==0):
            SumEvenFactors = SumEvenFactors+i
    print("Sum of even factors is", SumEvenFactors)

def DisplayOdd(No):
    SumOddFactors = 0
    for i in range(1,No+1):
        if(No%i==0 and i%2!=0):
            SumOddFactors = SumOddFactors+i
    print("Sum of odd factors is", SumOddFactors)

def main():
    value = int(input("Enter a number:"))
    start_time = time.perf_counter()
    t1 = threading.Thread(target=DisplayEven,args=(value,))
    t2 = threading.Thread(target=DisplayOdd,args=(value,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.perf_counter()
    print(f"Time required is {end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()
