
def DisplayStar(No):
    i = No

    while(i >= 1):
        j = 1

        while(j <= i):
            print("*", end=" ")
            j = j + 1

        print()
        i = i - 1

def main():
    value = int(input("Enter a number : "))
    DisplayStar(value)

if __name__ == "__main__":
    main()