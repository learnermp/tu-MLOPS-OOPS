# Common base class
class A:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello from A, my name is {self.name}.")

# Intermdeiate class 1
class B(A):
    def greet(self):
        print(f"Hello from B, my name is {self.name}.")
        super().greet()  # Call the base class method

# Intermdeiate class 2
class C(A):
    def greet(self):
        print(f"Hello from C, my name is {self.name}.")
        super().greet()  # Call the base class method

class D(B, C):
    def greet(self):
        print(f"Hello from D, my name is {self.name}.")
        super().greet()  # Call the method from B and C

# Create an instance of D
d = D("Charlie")
d.greet()  # This will call the greet method in D, which calls B and C's greet methods, and then A's greet method.
