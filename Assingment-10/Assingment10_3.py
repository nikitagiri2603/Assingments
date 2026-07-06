def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

def main():
    value = int(input("Enter number : "))
    result =  factorial(value)
    print("Factorial is : ",result)

if __name__ == "__main__":
    main()