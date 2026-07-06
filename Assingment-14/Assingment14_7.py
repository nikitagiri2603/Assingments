
dvisibleby5 = lambda No : True if No%5==0 else False

def main():
    value1 = int(input("Enter first number : "))
    Ret = dvisibleby5(value1)
    if(Ret):
        print("Number is Divisble by 5")
    else:
        print("Number is Not Divisible by 5")
        
if __name__ == "__main__":
    main()