#File Handling

open("filename", "mode")

#filename: The name or path of the file.
#mode: What you want to do with the file.

file = open("students.txt", "r") - #Read Mode

# Mode    Meaning	 What happens?

# "r"	  Read	     Reads an existing file
# "w"	  Write	     Creates a file or replaces its existing contents
# "a"	  Append	 Adds data to the end of a file
# "x"	  Create	 Creates a new file; errors if it already exists



file = open("students.txt", "w")

file.write("sama")

file.close()


with open("students.txt", "w") as file:
    file.write("Asha\n")
    file.write("Rahul\n")
    file.write("Meera\n")

print("File created successfully!")


#read
#read() reads the entire file and returns its contents as a string.
with open("students.txt", "r") as file:
    content = file.read()

print(content)


#Read one line — readline()
with open("students.txt", "r") as file:
    print(file.readline())
    print(file.readline())

#Read all lines into a list — readlines()

with open("students.txt", "r") as file:
    lines = file.readlines()

print(lines)

#Append data — "a"
#Adds new data to the end of a file without removing 
# existing contents.

with open("students.txt", "a") as file:
    file.write("Ali\n")

print("New student added!")

#Write multiple lines at once — writelines()

sun = ["Sara\n", "John\n", "Ravi\n"]

with open("students.txt", "w") as file:
    file.writelines(sun)

print("All names written!")


#Create a new file only — "x"
with open("courses.txt", "x") as file:
    file.write("Python\n")
    file.write("Data Science\n")

print("New file created!")