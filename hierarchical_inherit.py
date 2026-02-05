
# Base class
class Parent:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, my name is {self.name}.")\
        
# Derived class1
class Child1(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# Derived class2
class Child2(Parent):
    def work(self):
        print(f"{self.name} is working.")

# Create instances of Child1 and Child2
child1 = Child1("Alice")
child2 = Child2("Bob")

child1.greet()  # Inherited method from Parent  
child1.play()   # Method defined in Child1

child2.greet()  # Inherited method from Parent
child2.work()   # Method defined in Child2