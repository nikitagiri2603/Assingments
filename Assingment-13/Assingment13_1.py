def Area(length,width):
    Area = length * width
    return Area

def main():
    l = float(input("Enter length : "))
    b = float(input("Enter width: "))

    ret = Area(l,b)

    print("Area of rectangle is :",ret)

if __name__ == "__main__":
    main()