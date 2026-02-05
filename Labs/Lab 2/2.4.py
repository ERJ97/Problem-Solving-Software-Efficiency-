
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

# add data 

student1 = student("John", "12345", "Computer Science")
staff1 = staff("Jane", "54321", "Maths")

# add ID as a key 

directory[student1.ID_Number] = student1
directory[staff1.ID_Number] = staff1 

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



