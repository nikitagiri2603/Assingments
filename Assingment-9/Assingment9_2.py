def ChkGreater(no1,no2):
    if(no1>no2):
        print(no1,"is greater than ",no2)
    else:
        print(no2,"is greater than ",no1)

def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))

    ChkGreater(value1,value2)

if __name__=="__main__":
    main()