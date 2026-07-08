
import threading
def Thread1(No):
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    i = 1
    while(i<=50):
        print(i,end=" ")
        i = i+1
    print()


def Thread2(No):
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    i = 50
    while(i>=1):
        print(i,end=" ")
        i = i-1
    print()

def main():
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    value = int(input("Enter the number :"))
    t1 = threading.Thread(target=Thread1,args=(value,))
    t2 = threading.Thread(target=Thread2,args=(value,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()