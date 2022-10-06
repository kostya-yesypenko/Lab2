from math import gcd


class Rational:
    def __init__(self, numerator=1, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Wrong arguments")
        self.numerator = numerator // gcd(numerator, denominator)
        self.denominator = denominator // gcd(numerator, denominator)

    def float_form(self):
        return self.numerator / self.denominator

    def ab_form(self):
        return f'{self.numerator} / {self.denominator}'

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Rational(numerator, denominator)

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)


x = Rational(2, 4)
y = Rational()
z = x + y
print(x.float_form())
print(z.ab_form())
print(z.float_form())