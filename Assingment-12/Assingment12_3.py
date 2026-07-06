def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    return "Division is not possible (cannot divide by zero)."

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition =", addition(num1, num2))
    print("Subtraction =", subtraction(num1, num2))
    print("Multiplication =", multiplication(num1, num2))
    print("Division =", division(num1, num2))

if __name__ == "__main__":
    main()