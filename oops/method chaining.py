class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, x):
        self.value += x
        return self  # Returning self allows method chaining

    def subtract(self, x):
        self.value -= x
        return self  # Returning self allows method chaining

    def multiply(self, x):
        self.value *= x
        return self  # Returning self allows method chaining

    def divide(self, x):
        self.value /= x
        return self  # Returning self allows method chaining

# Using method chaining
result = Calculator(10).add(5).multiply(2).subtract(3).divide(4).value
print("Result:", result)  # Output: Result: 7.0
