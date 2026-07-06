import Arithmetic as calc

def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))

    retAdd = calc.Add(value1,value2)
    retSub = calc.Sub(value1,value2)
    retMult = calc.Mult(value1,value2)
    retDiv = calc.Div(value1,value2)

    print("Addition is :",retAdd)
    print("Subtraction is :",retSub)
    print("Multiplication is :",retMult)
    print("Division is :",retDiv)

if __name__ == "__main__":
    main()