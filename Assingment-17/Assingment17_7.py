
def DisplayStar(No):
    for i in range(1,No+1):
        for i in range(1,No+1):
            print(i,end = " ")
        print()

def main():
    value = int(input("Enter a number :"))
    DisplayStar(value)

if __name__ == "__main__":
    main()