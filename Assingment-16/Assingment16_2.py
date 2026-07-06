
def ChkNum(No):
    if(No % 2== 0):
        print(f"{No} is Even number")
    else:
        print(f"{No} is Odd number")

def main():
    value = int(input("Enter a number :"))
    ChkNum(value)

if __name__ == "__main__":
    main()
