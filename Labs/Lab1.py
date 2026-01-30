# Lists 

fruits = [] 

fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
fruits.append("date")

print("List after appending fruits:", fruits)

fruits.insert(1, "blueberry")
print("List after inserting blueberry at index 1: ", fruits)

print("Popped last fruit: ", fruits.pop())
print("List after popping last item", fruits)

print("Popped item at index 2: ", fruits.pop(2))
print("List after popping item at index 2: ", fruits)

fruits.sort()
print("List after sorting: ", fruits)

fruits.reverse()
print("List after reversing: ", fruits)

del fruits[0]
print("List after deleting the first item: ", fruits)

fruits.index("apple")
print("Index of apple: ", fruits.index("apple"))

print("Number of occurrences of 'cherry': ", fruits.count("cherry"))

fruits.remove("apple")
print("List after removing apple: ", fruits)


# Strings 

Sentance = "Python is a versatile programming language"
print(Sentance)

print("Number of occurrences of 'a': ", Sentance.count("a"))

print("Centered String: ", Sentance.center(60))

print("Left Justified String: ", Sentance.ljust(60))

print("Right Justified String: ", Sentance.rjust(60))

print("Uppercase String: ", Sentance.upper())

print("Lowercase String: ", Sentance.lower())

print("Index of 'versatile': ", Sentance.find("versatile"))

print("List of words: ", Sentance.split(" "))


# Tuples vs Lists 

tuple = (4, False, 5.3)
list = [4, False, 5.3]

print("Tuple: ", tuple)
print("List: ", list)

list[1] = True 
print("List with the item True: ", list)

# tuple[1] = True 
# print("Tuple with the item True", tuple)

list.insert(3, 888)
print("List after inserting 888: ", list)

# tuple.insert(3, 888)
# print("Tule after inserting 888:", tuple)

list.remove(888)
print("List after removing 888:", list)

# tuple.remove(888)
# print("Tuple after removing 888: ", tuple)

# Sets 

set_a = {True, 2, 3.5, 'apple'}
set_b = {3.5, 4, 5, 'banana', False}

print("set_a:", set_a)
print("set_b:", set_b)

print("Union of set_a and set_b: ", set_a.union(set_b))

print("Intersection of set_a and set_b:", set_a.intersection(set_b))

print("Items in set_a not in set_b: ", set_a.difference(set_b))

set_c = { 2,3.5,'apple'}
print("set_c:", set_c)

print("is set_c a subset of set_a?", set_c.issubset(set_a))

print("Updated set_a after adding 7.5: ", set_a.add(7.5))

print("Updated set_a after removing 'apple:", set_a.remove('apple'))

print("Popped item from set_b: ", set_b.pop())
print("Updated set_b after popping an item:", set_b)

set_a.clear()
print("set_a after cleaning: ", set_a)


# Operations: 

a = 10
b = 3 

print(a)
print(b)

print("Addition (a + b):", a + b)

print("Subtraciton (a - b):", a - b)

print("Multiplication (a * b): ", a * b)

print("Exponentiation (a ** b):", a ** b)

print("Division (a / b): ", a / b )

print("Integer Division (a // b): ", a // b )

print("Modulo (a % b): ", a % b )

print("Combined Operations (a + b * (a - b) / b ** 2):", a + b * (a - b) / b ** 2)
