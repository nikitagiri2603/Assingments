
def DisplayStar(No):
    for i in range(0,No):
        for i in range(0,No):
            print("*",end = " ")
        print()

def main():
    value = int(input("Enter a number :"))
    DisplayStar(value)

if __name__ == "__main__":
    main()