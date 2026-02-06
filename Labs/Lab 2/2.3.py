
access_codes = {
     'Peter': '9512',
     'Betsy': '7548', 
     'Cecilia': '2958', 
     'Lina': '5870', 
     'Laura': '4572',
     'Adele' : '8570', 
     'Luigi': '3572',
}

def search(code):
    for name, access_code in access_codes.items():
        if access_code == code:
            return name
    return None


def main():
    try:    
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

    except Exception as e: 
        print("Program Error!")

main()

# handel error 