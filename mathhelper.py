import math

class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def square(a):
        return a ** 2

    @staticmethod
    def square_root(a):
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(a)