
import threading
import time
def EvenList(Data):
    Sum = 0
    for no in Data:
        if(no%2==0):
            Sum = Sum + no
    print("Summation of even numbers in list: ",Sum)

def OddList(Data):
    Sum = 0
    for no in Data:
        if(no%2!=0):
            Sum = Sum + no
    print("Summation of odd numbers in list: ",Sum)

def main():
    Data = list()

    n = int(input("Enter how many elements you want in the list : "))

    for i in range(0, n):
        num = int(input())
        Data.append(num)

    print("Data is :", Data)

    t1 = threading.Thread(target=EvenList, args=(Data,))
    t2 = threading.Thread(target=OddList, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
if __name__ == "__main__":
    main()


    