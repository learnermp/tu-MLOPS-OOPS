# Base class
class GrandParent:
    def __init__(self, name):
        self.name = name
    def tell_story(self):
        print(f"{self.name} tells a story.")

# Intermediate class
class Parent(GrandParent):
    def work(self):
        print(f"{self.name} is working.")

# Derived class
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# Create an instance of Child
child = Child("Charlie")
child.tell_story()  # Inherited from Grandparent
child.work()        # Inherited from Parent