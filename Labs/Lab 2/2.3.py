
access_codes = [
    {'name': 'Peter', 'code': '9512'},
    {'name': 'Betsy', 'code': '7548'}, 
    {'name': 'Cecilia', 'code': '2958'}, 
    {'name': 'Lina', 'code': '5870'}, 
    {'name': 'Laura', 'code': '4572'},
    {'name': 'Adele', 'code': '8570'}, 
    {'name': 'Luigi', 'code': '3572'},
]

def search(query):
    for access in access_codes:
        if (access['code'] == query):
            return access['name']
    return None
        

try: 
    code = input("Enter access code: ")
    name = search(code) # stores returned dictionary name.  
    print(f"ACCESS GRANTED - Welcome {name}")
except LookupError:
    print("Incorrect, you have one attempt remaining. ") 


    try: 
        code = input("Enter access code: ")
        name = search(code)
        print(f"ACCESS GRANTED - Welcome {name}")
    except LookupError: 
        raise RuntimeError ("Access attempts failed.")
