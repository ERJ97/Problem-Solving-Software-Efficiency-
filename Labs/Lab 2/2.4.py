
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

directory = {}
 
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

# Search directory 

def search_member():
    print("--- Search directory --- ")
    ID = input("Enter ID to search: ")

    member = directory.get(ID)
    if member: 
        print("\n Match found: ")
        member.display() 
    else: 
        print("No match found")  


# Remove a member 

def remove_member():
    print("--- Remove member ---")
    ID = input("Enter ID to remove: ")  

    if ID in directory: 
        del directory[ID]
        print("Member removed successfully!")
    else: 
        print("No member exists with that ID.")

def view_directory(): 
    print(" --- Directory ---")
    if not directory: 
        print("Directory is empty.")
        return
    for ID, member in directory.items(): 
        print("-----")
        member.display()

# Main menu loop: 

def main(): 
    while True: 
        print("---------- Campus Directory - Menu ---------- ")
        print("1 - Add Member")
        print("2 - Search Member")
        print("3 - Remove Member")
        print("4 - View Directory")
        print("5 - Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_member()
        elif choice == "2":
            search_member()
        elif choice == "3":
            remove_member()
        elif choice == "4":
            view_directory()
        elif choice == "5":
            print("Exiting program.")
            break 
        else: 
            print("Invalid choice. Try again.")

main()


