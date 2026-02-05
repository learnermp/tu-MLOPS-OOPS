# base class
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# derived class
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# Create an instance of Child
child = Child("Alice")
child.greet()  # Inherited method from Parent
child.play()   # Method defined in Child