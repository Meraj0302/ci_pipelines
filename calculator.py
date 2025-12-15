class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


if __name__ == "__main__":
    calc = Calculator()
    print("Add:", calc.add(5, 3))
    print("Subtract:", calc.subtract(5, 3))
    print("Multiply:", calc.multiply(5, 3))
    print("Divide:", calc.divide(6, 3))
