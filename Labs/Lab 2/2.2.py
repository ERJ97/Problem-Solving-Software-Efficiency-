
extensions = [
    {'extension_no': '1250', 'location': 'Reception'},
    {'extension_no': '8754', 'location': 'IT Helpdesk'},
    {'extension_no': '5987', 'location': 'Library'},
    {'extension_no': '4128', 'location': 'Admissions'},
    {'extension_no': '9874', 'location': 'Coffee shop'},
    {'extension_no': '6548', 'location': 'Intelligent Robotics Lab'},
    {'extension_no': '3215', 'location': 'Robert Record Room'},
    {'extension_no': '6573', 'location': 'The Great Hall'},
    {'extension_no': '9512', 'location': 'Peter - office'},
    {'extension_no': '7548', 'location': 'Betsy - office'},
    {'extension_no': '2958', 'location': 'Cécilia - office'},
    {'extension_no': '5870', 'location': 'Lina - office'},
    {'extension_no': '4572', 'location': 'Laura - office'},
    {'extension_no': '8570', 'location': 'Adele - office'},
    {'extension_no': '3572', 'location': 'Luigi - office'},
]

def search(query):
    for extension in extensions: 
        if (extension['extension_no'] == query):
             return extension['location']
    # If the loop gets to here, no match was found. 
   
    raise LookupError("Extension not found, please try again.")

# Display all extensions: 

print("Valid extensions:")
for list in extensions:
    print("-", list['extension_no'], "--", list['location'])

# Attempt 1: 
try: 
    test1 = search(input("Eneter extension to contact:"))
    print("Extension found", test1)
except LookupError as e: 
    print("Lookup failed:", e)
    
    # Attempt 2: Inside the scope of Attempt 1, so if does not run unless 1 is invalid. 
    try: 
        test2 = search(input("Try again: "))
        print("Extension found!", test2)
    except LookupError: 
        raise RuntimeError("No valid extension.")

    
