
def DisplayPattern(No):
    for i in range(1, No + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    value = int(input("Enter a number : "))
    DisplayPattern(value)

if __name__ == "__main__":
    main()