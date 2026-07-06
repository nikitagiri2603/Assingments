def printFactors(num):
    for i in range(1,num+1):
        if(num%i==0):
            print(i,end=" ")

def main():
    value = int(input("Enter number : "))
    printFactors(value)

if __name__ == "__main__":
    main()