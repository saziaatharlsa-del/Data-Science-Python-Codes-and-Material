#---------------------DATA TYPE /COLLECTIONS/ DATA STRUCTURES----------------

# List
data = [10, 20, 20, 30]
new = [10, "sara", 20, 99.2]

# Tuple
mydata= (10, 20, "sara", 30)

# Set
data= {10, 20, "sara", 30}

# Dictionary
new= {"moon": 10, "sun": "sara","xyz": 30.6,"abc" : True}

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
students = ["Sara", "Ali", "John", "Emma"]

students.append("raheel")
print(students)


# Adding Elements - insert()
students = ["Sara", "Ali", "John", "Emma"]
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


students = ["Sara", "Ali", 30,  "John", "Emma"]
students.pop(1)
print(students)

# clear()
numbers = [10, 20, 30, 40]
numbers.clear()
print(numbers)

# List Methods - count()
students = ["Sara", "Ali", 30,  "John", "Emma"]
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

# List to Tuple

a = [10, 20, 30]

n= tuple(a)

print(n)

# Tuple to List

n= (10, 20, 30)

b = list(n)

print(b)

# SETS

# Creating a set
numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))

# Duplicate Values

numbers = {10, 20, 20, 30, 30, 40}

print(numbers)

# add()

numbers.add(10)
numbers.add(20)
numbers.add(30)

print(numbers)

# update()

numbers = {10, 20, 20, 30, 30, 40}

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

student = {
    "name": "Sara",
    "age": 20,
    "marks": 85
}

print(student["name"])
print(student["age"])
print(student["marks"])

# Adding a New Key-Value Pair

student = {
    "name": "Sara",
    "age": 20,
    "marks": 85
}

student["city"] = "Hyderabad"

print(student)

# Updating a Value

student = {
    "name": "Sara",
    "age": 20,
    "marks": 85
}

student["marks"] = 90

print(student)

# keys()

student = {
    "name": "Sara",
    "age": 20,
    "marks": 85
}

print(student.keys())
#keys() returns all keys.


# values()

student = {
    "name": "Sara",
    "age": 20,
    "marks": 85
}

print(student.values())
#values() returns all values.

# items()

student = {
    "name": "Sara",
    "age": 20,
    "marks": 85
}

print(student.items())

#items() returns each key-value pair as a tuple.


student = {
    "name": "Sara",
    "age": 20,
    "marks": 85
}


# get()


student = {
    "name": "Sara",
    "age": 20,
    "marks": 85
}

print(student.get("name"))
print(student.get("phone"))
print(student.get("phone", 937492))

# Avoids an error when key does not exist

student = {
    "name": "Sara",
    "age": 20,
    "marks": 85
}

print(student.get("phone", "Not Available"))
print(student.get("phone", 100))


# update()

student = {
    "name": "Sara",
    "age": 20,
    "marks": 85
}

student.update({
    "age": 21,
    "city": "Delhi"
})

print(student)

# pop()

student = {
    "name": "Sara",
    "age": 20,
    "marks": 85
}

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

#----------------------------------------------------------

# Membership in Lists

students = ["Sara", "Ali", "John"]

print("Sara" in students)
print("David" not in students)

# Looping Through a List

students = [10, 20, 30]

for i in students:
    print(i*i)

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

#new = [expression for item in iterable]

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)

# List Comprehension with Condition

#new= [expression for item in iterable if condition]

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

# Set Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))

# Set Intersection
print(set1.intersection(set2))


# Set Difference
print(set1.difference(set2))


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