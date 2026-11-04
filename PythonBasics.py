# PRINT()

print("Hello")
print("Hello Data Science")
print("Welcome to Python")

#This is a single-line comment

print("Python is easy to learn")  # This is an inline comment

# PYTHON IS CASE-SENSITIVE

name = "Sara"
Name = "Ali"

print(name)
print(Name)

#VARIABLES

name = "Mustafa"
name = "Raheel"
age = 20
marks = 85

print(name)
print(age)
print(marks)

# Changing a variable value
age = 21
print(age)

# Valid variable names:
name = "Sara"
student_name = "Sara"
student_name1 = "Sara"
studentName = "Sara"
_student = "Sara"

# Invalid variable names
# 2name = "Sara"          # Cannot start with a number
# student name = "Sara"  # Cannot contain spaces
# student-name = "Sara"  # Cannot use hyphen
# class = "Python"       # Cannot use Python keyword


#VARIABLES WITH CALCULATIONS

marks1 = 80
marks2 = 90

total = marks1 + marks2
average = total / 2

print("Total:", total)
print("Average:", average)


# DATA TYPES

name = "Sara"       # String
age = 20            # Integer
marks = 85.5        # Float
passed = True        # Boolean

print(name)
print(age)
print(marks)
print(passed)


name = 123.54
print(type(name))
print(type(age))
print(type(marks))
print(type(passed))

# NONE

result = None

print(result)
print(type(result))

# More examples

number = "10"
name = "hello"
number = int(number)
print(number)
print(name)

price = "99.50"
price = float(price)

number = 100
number = str(number)

print(type(number))

#String → int/float is possible if the string contains a valid numeric value.


# USER INPUT

#input() is designed to receive text from the user.

name = input("Enter your name: ")
print("Hello", name)

age = input("Enter your age: ")
print(type(age))

age = int(input("Enter your age: "))
print("Your age is:", age)


# TYPE CASTING

age = "20"

print(age)
print(type(age))

age = int(age)

print(age)
print(type(age))


# String to float

price = "99.50"

price = float(price)

print(price)
print(type(price))


# Number to string

number = 100

text = str(number)

print(text)
print(type(text))


# KEYWORDS

# if
# else
# elif
# for
# while
# def
# return
# True
# False
# None

# -----------------STRINGS----------------

name = "Sara"

print(name)
print(type(name))


# STRING CONCATENATION

first_name = 21
last_name = "Khan"

full_name = first_name + " " + last_name

print(full_name) 


# -----------------STRING METHODS------------------------------


#String Formatting

#String formatting means putting variables/values inside a string.

# method is f-strings:

name = "Sara"
age = 20

print(f"My name is {name} and I am {age} years old.")


# len() - LENGTH OF STRING

message = "Hello Data Science"

print(len(message))


# STRING INDEXING

name = "Python"

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# Negative indexing
print(name[-1])
print(name[-2])

# STRING SLICING

name = "Python"

print(name[0:3])
print(name[2:5])
print(name[:4])
print(name[2:])
print(name[:])

# Reverse string

name = "Python"

print(name[2::-1])

# lower()

name = "SARA"

print(name.lower())

# upper()

name = "sara"

print(name.upper())

# title()

name = "sara khan"

print(name.title())

# capitalize()

text = "python is easy to learn"

print(text.capitalize())

# strip()
# Removes spaces from both sides

text = "   Hello Python   "

print(text.strip())

# lstrip()
# Removes spaces from left side

text = "   Hello Python   "

print(text.lstrip())

# rstrip()
# Removes spaces from right side

text = "   Hello Python   "

print(text.rstrip())

# replace()

text = "I like Java"

new_text = text.replace("Java", "Python")

print(new_text)


# Replace spaces

text = "Hello World"

print(text.replace(" ", "-"))


# split()
# Converts string into a list


text = "Python is easy"

words = text.split()

print(words)


# Split using comma

text = "apple,banana,mango"

fruits = text.split(",")

print(fruits)


# join()
# Converts list into a string

words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)


# Join using hyphen

date_parts = ["2026", "10", "06"]

date = "-".join(date_parts)

print(date)


# find()

text = "Hello Python"

print(text.find("Python"))

print(text.find("Java"))


# count()

text = "banana"

print(text.count("a"))

print(text.count("n"))


# startswith()

text = "Python Programming"

print(text.startswith("Python"))

print(text.startswith("Java"))


# endswith()

filename = "report.pdf"

print(filename.endswith(".pdf"))

print(filename.endswith(".jpg"))


# isdigit()

age = "25"

print(age.isdigit())

age = "25abc"

print(age.isdigit())


# isalpha()

name = "Sara"

print(name.isalpha())

name = "Sara123"

print(name.isalpha())


# isalnum()
# Letters + numbers

value = "Sara123"

print(value.isalnum())

value = "Sara@123"

print(value.isalnum())


# STRING REVERSE

text = "Python"

reverse_text = text[::-1]

print(reverse_text)


#Escape Characters

#\n → New line

print("Hello\nWorld")

#\t → Tab space

print("Name\tAge")
print("Sara\t20")


# ABS()

number = -25

print(abs(number))


# ROUND()

price = 99.5678

print(round(price,2))

#ARITHMETIC OPERATORS

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)



# COMPARISON OPERATORS

age = 20

print(age > 18)
print(age < 18)
print(age >= 20)
print(age <= 20)
print(age == 20)
print(age != 20)


# LOGICAL OPERATORS

age = 20
marks = 80

# AND
print(age > 18 and marks > 50)

# OR
print(age > 18 or marks > 90)

# NOT
passed = True
print(not passed)


# IF STATEMENT

age = 20

if age >= 18:
    print("Adult")


# IF - ELSE

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")


# IF - ELIF - ELSE

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")



a = 10

if a > 5:
    print("Yes")
elif a < 5:
    print("No")
else:
    print("Equal")

# NESTED IF

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")


# FOR LOOP

for i in range(1, 6):
    print(i)



# range()

# range(5) gives 0 to 4

for i in range(5):
    print(i)


# Start and stop

for i in range(1, 6):
    print(i)


# Start, stop and step

for i in range(1, 11, 2):
    print(i)



# FOR LOOP WITH STRING

name = "Sara"

for letter in name:
    print(letter)



# WHILE LOOP

count = 1

while count <= 5:
    print(count)
    count = count + 1


# BREAK

for i in range(1, 11):

    if i == 5:
        break

    print(i)


# CONTINUE

for i in range(1, 6):

    if i == 3:
        continue

    print(i)


#Reverse 1234

number = 1234
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reverse:", reverse)


# EVEN OR ODD

number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Print the multiplication table

number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# Largest of three numbers
a = 25
b = 40
c = 15

if a > b and a > c:
    print("A is largest")
elif b > a and b > c:
    print("B is largest")
else:
    print("C is largest")



# Count digits in a number

number = 12345
count = 0

while number > 0:
    number = number // 10
    count = count + 1

print("Number of digits:", count)



#--------------------- DATA TYPE /COLLECTIONS/ DATA STRUCTURES----------------

# List
my_list = [10, 20, 20, 30]

# Tuple
my_tuple = (10, 20, 20, 30)

# Set
my_set = {10, 20, 20, 30}

# Dictionary
my_dict = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(my_list)
print(my_tuple)
print(my_set)
print(my_dict)


# LISTS

students = ["Sara", "Ali", "John", "Emma"]
print(students)

data = ["Sara", 20, 85.5, True]
print(data)

# Length of a list
print(len(students))

# List Indexing

print(students[0])
print(students[1])
print(students[-1])

# List Slicing

print(students[0:2])
print(students[1:3])
print(students[:3])
print(students[2:])
print(students[:])

# Updating List Elements

students[1] = "Ahmed"
print(students)

# Adding Elements - append()

students.append("David")
print(students)


# Adding Elements - insert()

students.insert(1, "Rahul")
print(students)


# Adding Multiple Elements - extend()

students.extend(["Maya", "Noah"])
print(students)


# Removing Elements - remove()

students.remove("David")
print(students)


# Removing Elements - pop()

students.pop()
print(students)

students.pop(1)
print(students)


# clear()

numbers = [10, 20, 30, 40]
numbers.clear()
print(numbers)


# List Methods - count()

numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))


# List Methods - index()

numbers = [10, 20, 30, 40]
print(numbers.index(30))


# sort()

numbers = [50, 10, 40, 20, 30]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)


# reverse()

numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)


# copy()

original = [10, 20, 30]
copied = original.copy()

print(original)
print(copied)


# List Concatenation

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2
print(result)


# List Repetition

numbers = [1, 2, 3]

print(numbers * 2)


# Membership in Lists

students = ["Sara", "Ali", "John"]

print("Sara" in students)
print("David" not in students)


# Looping Through a List

students = ["Sara", "Ali", "John"]

for student in students:
    print(student)


# Built-in Functions with Lists

numbers = [10, 20, 30, 40, 50]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

# Nested Lists

students = [
    ["Sara", 20, 85],
    ["Ali", 21, 90],
    ["John", 19, 75]
]

print(students)
print(students[0])
print(students[0][0])
print(students[1][2])

# List Comprehension


#new_list = [expression for item in iterable]

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)



# List Comprehension with Condition

#new_list = [expression for item in iterable if condition]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)


# 1. Transform

numbers = [1, 2, 3]

result = [n * 2 for n in numbers]

print(result)


# 2. Filter
numbers = [1, 2, 3, 4, 5]

result = [n for n in numbers if n > 3]

print(result)


# 3. Transform + Filter

numbers = [1, 2, 3, 4, 5]

result = [n * 2 for n in numbers if n > 2]

print(result)

#-----------------------------------------------------------------------


# TUPLES

# Creating a tuple
students = ("Sara", "Ali", "John", "Emma")

print(students)
print(type(students))
print(len(students))


# Tuple Indexing

print(students[0])
print(students[1])
print(students[-1])


# Tuple Slicing

print(students[0:2])
print(students[1:3])
print(students[:3])
print(students[2:])
print(students[:])


# Tuple with Duplicate Values

numbers = (10, 20, 10, 30, 10)

print(numbers)

# count()

print(numbers.count(10))

# index()

print(numbers.index(20))


# Tuple Concatenation

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)


# Tuple Repetition

numbers = (1, 2, 3)

print(numbers * 2)


# Tuple Unpacking

student = ("Sara", 20, 85)

name, age, marks = student

print(name)
print(age)
print(marks)


# Single-Item Tuple
number = (10,)

print(number)
print(type(number))


# Without comma, it is not a tuple
number = (10)

print(number)
print(type(number))


# Tuple Membership

numbers = (10, 20, 30, 40)

print(20 in numbers)
print(50 not in numbers)


# Looping Through a Tuple

students = ("Sara", "Ali", "John")

for student in students:
    print(student)


# Nested Tuple

students = (
    ("Sara", 20, 85),
    ("Ali", 21, 90),
    ("John", 19, 75)
)

print(students)
print(students[0])
print(students[0][0])
print(students[1][2])


# Built-in Functions with Tuples

numbers = (10, 20, 30, 40, 50)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))


# List to Tuple

numbers_list = [10, 20, 30]

numbers_tuple = tuple(numbers_list)

print(numbers_tuple)


# Tuple to List

numbers_tuple = (10, 20, 30)

numbers_list = list(numbers_tuple)

print(numbers_list)


# SETS

# Creating a set
numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))


# Duplicate Values

numbers = {10, 20, 20, 30, 30, 40}

print(numbers)


# Creating Empty Set

numbers = set()

print(numbers)
print(type(numbers))


# add()

numbers.add(10)
numbers.add(20)
numbers.add(30)

print(numbers)

# update()

numbers.update([40, 50, 60])

print(numbers)

# remove()

numbers.remove(60)

print(numbers)


# discard()

numbers.discard(100)

print(numbers)


# pop()

numbers = {10, 20, 30, 40}

removed = numbers.pop()

print("Removed:", removed)
print(numbers)


# clear()

numbers = {10, 20, 30}

numbers.clear()

print(numbers)


# Set Union

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))


# Union Operator
print(set1 | set2)


# Set Intersection

print(set1.intersection(set2))

# Intersection Operator
print(set1 & set2)


# Set Difference

print(set1.difference(set2))

# Difference Operator
print(set1 - set2)


# Symmetric Difference

print(set1.symmetric_difference(set2))

# Symmetric Difference Operator
print(set1 ^ set2)


# Subset

a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))


# Superset

print(b.issuperset(a))


# Disjoint Sets

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))


# Set Membership

numbers = {10, 20, 30, 40}

print(20 in numbers)
print(50 not in numbers)


# Looping Through a Set

numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)


# Length of Set

print(len(numbers))


# List to Set

numbers = [10, 20, 20, 30, 30, 40]

unique_numbers = set(numbers)

print(unique_numbers)


# Set to List

numbers = {10, 20, 30}

numbers_list = list(numbers)

print(numbers_list)


# DICTIONARIES

# Creating a dictionary
student = {
    "name": "Sara",
    "age": 20,
    "marks": 85
}

print(student)
print(type(student))

# Accessing Dictionary Values

print(student["name"])
print(student["age"])
print(student["marks"])


# Adding a New Key-Value Pair

student["city"] = "Hyderabad"

print(student)


# Updating a Value

student["marks"] = 90

print(student)


# keys()

print(student.keys())


# values()

print(student.values())


# items()

print(student.items())


# get()

print(student.get("name"))
print(student.get("phone"))

# Avoids an error when key does not exist
print(student.get("phone", "Not Available"))


# update()

student.update({
    "age": 21,
    "city": "Delhi"
})

print(student)


# pop()

student.pop("city")

print(student)


# popitem()

student = {
    "name": "Sara",
    "age": 20,
    "marks": 85
}

removed = student.popitem()

print("Removed:", removed)
print(student)


# setdefault()

student = {
    "name": "Sara",
    "age": 20
}

student.setdefault("city", "Hyderabad")

print(student)


# clear()

student.clear()

print(student)


# copy()

student = {
    "name": "Sara",
    "age": 20
}

student_copy = student.copy()

print(student)
print(student_copy)


# Dictionary Membership

student = {
    "name": "Sara",
    "age": 20,
    "marks": 85
}

print("name" in student)
print("city" not in student)


# Loop Through Dictionary Keys

for key in student:
    print(key)


# Loop Through Dictionary Values

for value in student.values():
    print(value)


# Loop Through Key-Value Pairs

for key, value in student.items():
    print(key, value)


# Nested Dictionary

students = {
    "student1": {
        "name": "Sara",
        "age": 20,
        "marks": 85
    },

    "student2": {
        "name": "Ali",
        "age": 21,
        "marks": 90
    }
}

print(students)

print(students["student1"])
print(students["student1"]["name"])
print(students["student2"]["marks"])


# Dictionary with List

student = {
    "name": "Sara",
    "subjects": ["Python", "SQL", "Statistics"],
    "marks": [85, 90, 80]
}

print(student)
print(student["subjects"])
print(student["subjects"][0])

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




