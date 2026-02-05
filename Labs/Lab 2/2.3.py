
access_codes = [
    {'name': 'Peter', 'code': '9512'},
    {'name': 'Betsy', 'code': '7548'}, 
    {'name': 'Cecilia', 'code': '2958'}, 
    {'name': 'Lina', 'code': '5870'}, 
    {'name': 'Laura', 'code': '4572'},
    {'name': 'Adele', 'code': '8570'}, 
    {'name': 'Luigi', 'code': '3572'},
]

def search(code):
    for access in access_codes:
        if (access['code'] == code):
            return access['name']
    return None



def main():
    attempts = 2

    try:
        # Attempt 1
        code = input("Enter access code: ")
        name = search(code)

        if name is None:
            raise LookupError("Invalid code")

        print(f"ACCESS GRANTED - Welcome {name}")
        return

    except LookupError:
            print("Incorrect, you have one attempt remaining.")

    # Attempt 2
    code = input("Enter access code: ")
    name = search(code)

    if name is None:
        raise RuntimeError("Access attempts failed.")

    print(f"ACCESS GRANTED - Welcome {name}")


main()
