
def Display(No):
    for i in range(0,No):
        print("*", end=" ")

def main():
    value = int(input("Enter a number :"))
    Display(value)

if __name__ == "__main__":
    main()