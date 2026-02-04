class Employee:
    # special/madic/dunder/ method - constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 398273
        self.designation = "MLOPs Engineer"
        print("attributes/data have been initialised/executed")
    def travel(self, destination):
        print("this travel method was called manually")
        print(f"Employee is now travelling to {destination}")
# Create an instance/object of this class


if __name__ == "__main__":
    destination = "Bangalore"
    sam = Employee()
    sam.travel(destination)
    print(type(sam))