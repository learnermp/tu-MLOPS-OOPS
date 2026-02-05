# Base class
class Animal:
    def __init__(self, name = "Ranveer"):
        self.name = "Buddy"

    def sound(self):
        print(f"{self.name} makes a sound.")

# Intermediate Class 1 (Hierarchical Inheritance)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

# Intermediate Class 2 (Multiple Inheritance)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# Derived class (Multiple Inheritance)
class Dog(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name) # Initialize Mammal part; Explicit parent constructor calls bypass super()
    
    def nocturnal(self):
        print(f"{self.name} is active at night.")

# Create an instance of Dog
dog = Dog("Charlie")
dog.sound()      # Inherited from Animal
dog.feed()       # Inherited from Mammal
dog.fly()        # Inherited from Bird
dog.nocturnal()  # Method defined in Dog 