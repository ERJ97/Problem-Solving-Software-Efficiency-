# 2.1

students =[ 
    {'name': 'Cecilia', 'student_number': '1255', 'telephone_number': '5555501'},
    {'name': 'Betsy', 'student_number': '1254', 'telephone_number': '5555502'},
    {'name': 'Lina', 'student_number': '1256', 'telephone_number': '5555503'},
    {'name': 'Laura', 'student_number': '1257', 'telephone_number': '5555504'},
    {'name': 'Adele', 'student_number': '1258', 'telephone_number': '5555505'},
]

try: 
    user_validation = input("Input search request: ").strip() # removed whitespace - validation 

    if user_validation.isdigit():
        query = user_validation
    else: 
        query = user_validation.lower()

    def search(query):
        for student in students: 
            if (student['name'].lower() == query or
                student['student_number'] == query or
                student['telephone_number'] == query):
                return student
        return None 
    
    userInput = search(query)
    print("Information found: ", userInput)

except LookupError as e:
    print("No student match", e)

