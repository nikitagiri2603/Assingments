
import threading

def DisplaySmall(str1):
    print("Thread Id is ",threading.get_ident())
    print("Name of current thraed is :",threading.current_thread().name)
    cnt = 0
    for i in str1:
        if(i>='a' and i<='z'):
            cnt = cnt + 1
    print(f"Lowercase letters in {str1} is {cnt}")

def DisplayCapital(str1):
    print("Thread Id is ",threading.get_ident())
    print("Name of current thraed is :",threading.current_thread().name)
    cnt = 0
    for i in str1:
        if(i>='A' and i<='Z'):
            cnt = cnt + 1
    print(f"Uppercase letters in {str1} is {cnt}")

def DisplayDigits(str1):
    print("Thread Id is ",threading.get_ident())
    print("Name of current thraed is :",threading.current_thread().name)
    cnt = 0
    for i in str1:
        if(i >= '0' and i <= '9'):
            cnt = cnt + 1
    print(f"Digits in {str1} is {cnt}")   

def main():
    print("Thread ID of main thread :", threading.get_ident())
    string = input("Enter a alphanumeric string :")
    
    t1 = threading.Thread(target=DisplaySmall,args=(string,))
    t2 = threading.Thread(target=DisplayCapital,args=(string,))
    t3 = threading.Thread(target=DisplayDigits,args=(string,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()