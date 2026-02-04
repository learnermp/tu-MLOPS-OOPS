class Employee:
    # special/madic/dunder/ method - constructor
    def __init__(self):
        print(f"id of self is : {id(self)}")
        print("Started executing attributes/data")
        self. __name = "Default name"
        self.id = 123
        self.salary = 398273
        self.designation = "MLOPs Engineer"
        print("attributes/data have been initialised/executed")
    def travel(self, destination):
        print("this travel method was called manually")
        print(f"Employee is now travelling to {destination}")
# Create an instance/object of this class


if __name__ == "__main__":
    sam = Employee()

    sam.name = "Shammi Kapoor"      # Creating variable outside constructor
    print(f"id of object sam is : {id(sam)}")
    sam.travel("Bangalore")
    print(f"sam's name is : {sam.name}")
    # print(f" sam.__name will raise an AttributeError: {sam.__name}")  # will raise an AttributeError
    print(sam._Employee__name)  # name mangling to access private variable
    print('''========================================
             ========================================''')
    mam = Employee()
    print(f"id of object mam is : {id(mam)}")
    mam.travel("Kerela")
