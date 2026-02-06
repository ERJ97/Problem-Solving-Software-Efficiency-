
# Needs cleaning up. Have the add logic function but now need to add a main.


# Superclass Campus Member 
class campus_member:
    def __init__(self, name, ID_Number):
        self.name = name
        self.ID_Number = ID_Number

    def display(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.ID_Number}")

# Student - subclass 

class student(campus_member):
    def __init__(self, name, ID_Number, degree_program):
        # Call superclass and inherit 
        super().__init__(name, ID_Number)

        self.degree_program = degree_program 

        # Display degree with info from super 
    def display(self):
        super().display()
        print(f"Degree Programme:  {self.degree_program}")


# Staff - subclass 
class staff(campus_member): 
    def __init__(self, name, ID_Number, department):
        super().__init__(name, ID_Number)
        self.department = department
    
    # Override display to include deparment: 
    def display(self):
        super().display()
        print(f"Department: {self.department}")

# must use {} not []
directory = {}


# add ID as a key 

#directory[student1.ID_Number] = student1
#directory[staff1.ID_Number] = staff1 

def search(ID):
    if ID in directory: 
        return directory[ID]
    else: 
        print("ID does not exist in directory")
        return None
    
# Search directory 

ID = input("Enter ID to search: ")
member = search(ID)

if member:
    member.display()

    # add bit to make you able to do this in the terminal. 
    # As in add objects to directory, then an option to search 


def add_member():
    print("Add new campus member \n")
    name = input("Enter name:")
    ID = input("Enter ID: ")

    if ID in directory:
        print("That ID already exists in directory")
        return 

    member_type = input("Student or Staff?").strip().lower()
    
    if member_type == "student":
        degree = input("Degree program: ")
        directory[ID] = student(name, ID, degree)

    elif member_type == "staff": 
        department = input("Deparment: ")
        directory[ID] = staff(name, ID, department)

    else: 
        print("Invalid")
        return

    print("Member added successfully!")


