#JSON stands for JavaScript Object Notation. 
# It stores structured data using key-value pairs and lists.

import json

student = {
    "student_id": 1,
    "name": "Asha",
    "course": "Python",
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully!")

#import json imports the JSON module.
#json.dump() writes Python data into a JSON file.
#indent=4 formats the file neatly for readability.

#Read data from a JSON file

import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student)
print(student["name"])
print(student["marks"])

#json.load() reads the JSON file and converts the data into a Python dictionary.

#Store multiple students in JSON

import json

students = [
    {"name": "Asha", "course": "Python", "marks": 85},
    {"name": "Ravi", "course": "SQL", "marks": 70},
    {"name": "Sara", "course": "Python", "marks": 90}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Student records saved!")


#Read and filter JSON records

#Print only Python students who scored above 80.

import json

with open("students.json", "r") as file:
    students = json.load(file)

for i in students:
    if i["course"] == "Python" and i["marks"] > 80:
        print(i["name"], i["marks"])


#Feature	               CSV	                     JSON

#Structure	         Rows and columns	          Objects and lists
#Best suited for	   Tabular data	           Structured or nested data
#Python module	           csv	                       json
#Common use	        Excel-like datasets	       APIs and application data