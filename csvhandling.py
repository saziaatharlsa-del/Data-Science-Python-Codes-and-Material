#Write data into a CSV file
import csv
students = [    
    [1, "Asha", "Python", 85],    
    [2, "Ravi", "SQL", 70],    
    [3, "Sara", "Python", 90]]

with open("students.csv", "w", newline="") as file:    
    moon = csv.writer(file)    
    moon.writerow(["student_id", "name", "course", "marks"])    
    moon.writerows(students)
print("CSV file created successfully!")

#- import csv imports the CSV module.
#- "students.csv" is the filename.
#- "w" opens the file in write mode, creating it if necessary and replacing existing contents.
#- csv.writer(file) creates a writer object.
#- writerow() writes one row.
#- writerows() writes multiple rows.

#- newline="" helps prevent extra blank lines on some systems.

#Read data from a CSV file

import csv
with open("students.csv", "r", newline="") as file:    
    root = csv.reader(file)    
    for i in root:        
        print(i)

#values read from a CSV file are returned as strings.

#Read CSV using column names

#DictReader makes each row available as a dictionary.

import csv
with open("students.csv", "r", newline="") as file:    
    reader = csv.DictReader(file)    
    for i in reader:        
        print(i["name"], i["marks"])


#Filter student records
#Print only students who scored above 80.

import csv
with open("students.csv", "r", newline="") as file:    
    reader = csv.DictReader(file)    
    for i in reader:        
        if int(i["marks"]) > 80:            
            print(i["name"], i["marks"])


#We use int() because CSV values are initially read as strings.