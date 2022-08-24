from math import atan, sqrt

class complexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary
        
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def conjugate(self):
        return complexNumber(self.real, -self.imaginary)
    
    def modargform(self):
        a,b = self.real, self.imaginary
        r = str(sqrt(a**2 + b**2))
        theta = str(atan(b/a))
        return f"{r}(cos({theta}) + isin({theta}))"


    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return complexNumber(real, imaginary)

    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return complexNumber(real, imaginary)

    def __mul__(self, other):
        a,b,c,d = self.real, self.imaginary, other.real, other.imaginary
        real = a*c - b*d
        imaginary = a*d + b*c
        return complexNumber(real, imaginary)

    def __truediv__(self, other):
        a,b,c,d = self.real, self.imaginary, other.real, other.imaginary
        real = (a*c + b*d)/(c**2 + d**2)
        imaginary = (-a*d + b*c) / (c**2 + d**2)
        return complexNumber(real, imaginary)

i = complexNumber(0, 1)

a = complexNumber(4, 2)
b = complexNumber(3, 5)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a.conjugate())
print(a.modargform())
