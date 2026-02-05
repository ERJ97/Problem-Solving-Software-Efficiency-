# 2.1

students =[ 
    {'name': 'Cecilia', 'student_number': '1255', 'telephone_number': '5555501'},
    {'name': 'Betsy', 'student_number': '1254', 'telephone_number': '5555502'},
    {'name': 'Lina', 'student_number': '1256', 'telephone_number': '5555503'},
    {'name': 'Laura', 'student_number': '1257', 'telephone_number': '5555504'},
    {'name': 'Adele', 'student_number': '1258', 'telephone_number': '5555505'},
]

# define function: 

def search(query):
    for student in students: 
        if (student['name'] == query or
            student['student_number'] == query or
            student['telephone_number'] == query):
            return student
    return None

# loop scope is defined by indentation!

test1 = search('Lina')
print(test1)

test2 = search('1258')
print(test2)

test3 = search('5555501')
print(test3)

