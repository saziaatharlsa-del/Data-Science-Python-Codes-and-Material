# List Comprehension

#new = [expression for item in iterable]

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)

# List Comprehension with Condition

#new= [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)

# 1. Transform

numbers = [1, 2, 3]

result = [n * 2 for n in numbers]

print(result)

# 2. Filter

numbers = [1, 2, 3, 4, 5]

result = [n for n in numbers]
rsult= [4,5]
result = [n*3 for n in numbers]
rsult= []

result = []


print(result)

# 3. Transform + Filter

numbers = [1, 2, 3, 4, 5]

result = [n * 2 for n in numbers if n > 2]

print(result)

# Dictionary Comprehension

numbers = [1, 2, 3, 4, 5]

squares = {x: x * x for x in numbers}

print(squares)

# Dictionary Comprehension with Condition

even_squares = {
    x: x * x
    for x in numbers
    if x % 2 == 0
}

print(even_squares)


#=================================================================


# 1. Create a list of numbers

numbers = [x for x in range(1, 6)]
print(numbers)

# 2. Find squares of numbers

squares = [x ** 2 for x in range(1, 6)]
print(squares)

# 3. Convert names to uppercase

names = ["asha", "rahul", "sara"]
upper_names = [name.upper() for name in names]
print(upper_names)

# 4. Select even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [x for x in numbers if x % 2 == 0]
print(evens)

# 5. Select numbers greater than 10

numbers = [5, 12, 8, 20, 15, 3]
result = [x for x in numbers if x > 10]
print(result)

# 6. Convert temperatures from Celsius to Fahrenheit

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(fahrenheit)

# 7. Extract names of students who passed

marks = [85, 35, 72, 45, 90]
passed_marks = [m for m in marks if m >= 50]
print(passed_marks)


#----------------------------------------------------

# 1. Create a dictionary of numbers and their squares

squares = {x: x**2 for x in range(1, 6)}
print(squares)


# 2. Convert two lists into a dictionary

names = ["Asha", "Rahul", "Sara"]
marks = [85, 90, 78]
result = {names[i]: marks[i] for i in range(len(names))}
print(result)

# 3. Dictionary comprehension with a condition
    
#Suppose we want only students who scored at least 50.

marks = {    "Asha": 85,    "Rahul": 35,    "Sara": 90,    "John": 42}
passed = {    name: mark    for name, mark in marks.items()    if mark >= 50}
print(passed)

#Suppose we have students' marks:
marks = {    "Asha": 85,    "Rahul": 35,    "Sara": 90,    "John": 42}

#- Marks greater than or equal to 50 → "Pass"
#- Marks below 50 → "Fail"
#create a new dictionary that stores each student's name and result.

#Expected output:
{    'Asha': 'Pass',    'Rahul': 'Fail',    'Sara': 'Pass',    'John': 'Fail'}


#First solve it using a normal for loop
marks = {    "Asha": 85,    "Rahul": 35,    "Sara": 90,    "John": 42}
results = {}
for name, mark in marks.items():    
    if mark >= 50:        
        results[name] = "Pass"    
    else:        
        results[name] = "Fail"
print(results)

#1. marks.items() gives us each student's name and marks.
#2. name stores the student's name.
#3. mark stores the student's marks.
#4. if mark >= 50 checks whether the student passed.
#5. results[name] = "Pass" adds the name and "Pass" to the dictionary.
#6. Otherwise, "Fail" is added.

#when the loop processes Asha:
name = "Asha"
mark = 85

#Since 85 >= 50 is True, the dictionary becomes:
{"Asha": "Pass"}

#The loop repeats for every student.
    
#Convert it into dictionary comprehension

results = {    name: "Pass" if mark >= 50 else "Fail"    for name, mark in marks.items()}
print(results)

#Output:
{'Asha': 'Pass', 'Rahul': 'Fail', 'Sara': 'Pass', 'John': 'Fail'}

#Dictionary comprehension structure

{key: value_if_true if condition else value_if_false for item in iterable}

#name — the dictionary key (student's name).

#"Pass" — the value when the condition is true.

#mark >= 50 — the condition being checked.

#"Fail" — the value when the condition is false.

for name, mark in marks.items() — processes each name and mark.

#4. Create a dictionary of even numbers and their squares

result = {    x: x**2    for x in range(1, 11)    if x % 2 == 0}
print(result)

#5. Convert names to uppercase

names = ["asha", "rahul", "sara"]
result = {name: name.upper() for name in names}
print(result)

#6. Use if-else in dictionary comprehension

#Suppose marks of 50 or above mean Pass; otherwise, Fail.

marks = {"Asha": 85,    
         "Rahul": 35,    
         "Sara": 90,    
         "John": 42}

results = {    name: "Pass" if mark >= 50 else "Fail"    for name, mark in marks.items()}
print(results)