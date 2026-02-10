
extensions = {
     '1250': 'Reception',
     '8754': 'IT Helpdesk',
     '5987': 'Library',
     '4128': 'Admissions',
     '9874': 'Coffee shop',
     '6548': 'Intelligent Robotics Lab',
     '3215': 'Robert Record Room',
     '6573': 'The Great Hall',
     '9512': 'Peter - office',
     '7548': 'Betsy - office',
     '2958': 'Cécilia - office',
     '5870': 'Lina - office',
     '4572': 'Laura - office',
     '8570': 'Adele - office',
     '3572': 'Luigi - office',
}
# add input validation?
def search(query): 
        if query in extensions:
             return extensions[query]
    # If the loop gets to here, no match was found. 
        raise LookupError("Extension not found, please try again.")

try:
# Attempt 1: 
    try: 
        test1 = search(input("Eneter extension to contact:"))
        print("Extension found", test1)
    except LookupError as e: 
        print("Lookup failed.\n", e)

    print("Valid extensions:")
    for ext_no, location in extensions.items(): 
        # items returns a sequence of 2-element tuples. 
        print("-", ext_no, "--", location) 
        
        # Attempt 2: Inside the scope of Attempt 1, so if does not run unless 1 is invalid. 
    try: 
        test2 = search(input("Try again: "))
        print("Extension found!", test2)
    except LookupError: 
        raise RuntimeError("No valid extension.")

except Exception as e: 
     print("Program error occoured.")
    # handle error (try catch)
