def Area(radius, PI = 3.14):
    Area = PI * radius * radius
    return Area

def main():
    Radius = int(input("Enter radius :"))
    area = Area(Radius)
    print("Area of circle is :",area)

if __name__ == "__main__":
    main()