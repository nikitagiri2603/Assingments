def Cube(num):
    result = num * num * num
    print("Cube of number is : ",result)

def main():
    value = int(input("Enter first number : "))
    Cube(value)

if __name__=="__main__":
    main()
