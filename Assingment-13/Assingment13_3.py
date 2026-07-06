
def CheckPerfect(no):
    original = no
    sum = 0
    for i in range(1,no):
        if(no % i ==0):
            sum = sum + i 

    if(original == sum):
        return True
    else:
        return False

def main():
    Value = int(input("Enter a number :"))
    ret = CheckPerfect(Value)
    if(ret == True):
        print(Value,"is perfect number")
    else:
        print(Value,"is Not perfect number")

if __name__ == "__main__":
    main()