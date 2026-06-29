def displayNumbers(num):
    for i in range(1, num + 1):
        print(i, end=" ")

def main():
    value = int(input("Enter a number: "))
    displayNumbers(value)

if __name__ == "__main__":
    main()