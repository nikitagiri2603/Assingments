def printEven(num):
    for i in range(1,num+1):
        if(i%2 ==0):
            print(i,end=" ")

def main():
    value = int(input("Enter the number : "))
    printEven(value)

if __name__ == "__main__":
    main()