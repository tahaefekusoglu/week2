class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return self.a + self.a + self.b + self.b

Rec = Rectangle(a=8, b=9)

print("Area:", Rec.area())
print("Perimeter", Rec.perimeter())


