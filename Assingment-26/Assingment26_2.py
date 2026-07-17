
class Circle:
    PI = 3.14
    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self):
        self.radius = float(input("Enter radius of the circle :"))

    def CalculateArea(self):
        self.area = Circle.PI * self.radius * self.radius

    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius 

    def Display(self):
        print(f"Value of radius is : {self.radius}")
        print(f"Value of area is : {self.area}")
        print(f"Value of circumference is : {self.circumference}")

c1 = Circle()
c1.Accept()
c1.CalculateArea()
c1.CalculateCircumference()
c1.Display()

c2 = Circle()
c2.Accept()
c2.CalculateArea()
c2.CalculateCircumference()
c2.Display()