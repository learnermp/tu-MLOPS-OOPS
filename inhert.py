class Animal:
    def __init__(self, name):
        self.name = name
        self.style = "stylish"

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def __init__(self, name, age):
        
        super().__init__(name)   # call parent constructor
        self.behaviour = "Friendly"
        self.age = age

    def speak(self):  # overriding
        print(f"{self.name} says Woof")

    def speak2(self):  # new method
        print(f"{self.name} is {self.age} years old and has a {self.behaviour} behaviour and {self.style} style.")

dog = Dog("Buddy", 16)
print(dog.name)
dog.speak()
dog.speak2() 