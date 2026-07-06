
def DisplayEven(No):
    for i in range(1,No+1):
        if(i % 2==0):
            print(i,end=" ")

def main():
    value = int(input("Enter a number :"))
    DisplayEven(value)

if __name__ == "__main__":
    main()