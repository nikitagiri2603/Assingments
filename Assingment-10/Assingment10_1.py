def Multiplication(num):
    for i in range(1,11):
        print(num," x ",i," = ",num*i)


def main():
    number = int(input("Enter a number :"))
    Multiplication(number)


if __name__ == "__main__":
    main()