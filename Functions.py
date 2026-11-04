print("Hello Sara")
print("Hello Ali")
print("Hello John")

def greet():
    print("Hello")

greet()
greet()
greet()

#Function with a parameter

#A parameter allows us to give information to the function.

def greet(name):
    print("Hello", name)

greet("Sara")
greet("Ali")

#name is the parameter.

#"Sara"
#"Ali" are arguments.

#Parameter = variable in the function definition
#Argument = actual value passed when calling the function

#Multiple parameters

def add(a, b):
    print(a + b)

add(10, 20)
add(5, 7)

#return sends a result back to the place where the function was called.

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

#print vs return

def add(a, b):
    print(a + b)

#This displays the answer.

def add(a, b):
    return a + b

#This gives the answer back, so we can store or use it.

def add(a, b):
    return a + b

result = add(10, 20)

print(result * 2)

#Function with no parameter and no return

def welcome():
    print("Welcome to Python")

welcome()

#Parameter but no return

def greet(name):
    print("Hello", name)

greet("Sara")

#Parameter and return

def square(number):
    return number * number

result = square(5)

print(result)

#Default parameter

def greet(name="Student"):
    print("Hello", name)

greet()
greet("Sara")

def calculate_total(m1, m2, m3):
    total = m1 + m2 + m3
    return total

def calculate_percentage(total):
    return total / 300 * 100

marks = calculate_total(80, 90, 85)
percentage = calculate_percentage(marks)

print("Total Marks:", marks)
print("Percentage:", percentage)


#Types of arguments in Python

#Python supports several ways to pass arguments.

#A. Positional arguments

#Values are assigned according to their position.
def student(name, age):    
    print(name, age)

student(20, "Ali")


#If the order changes, the result changes:

student(20, "Ali")

#B. Keyword arguments

#Pass values by specifying parameter names.

def student(name, age):    
    print(name)    
    print(age)

student(age=20, name="Ali")


#C. Default arguments

#A parameter uses a default value when no argument is supplied for it.

def greet(name="Student"):    
    print("Hello", name)

greet()
greet("Ahmed")


#D. Variable-length positional arguments — *args

#Use *args when a function should accept any number of positional arguments.


def add_numbers(*args):    
    print(args)    
    print("Total:", sum(args))
    
add_numbers(10, 20)
add_numbers(10, 20, 30, 40)

#- args is a tuple inside the function.
#- The * allows multiple positional arguments.


#E. Variable-length keyword arguments — **kwargs

#Use **kwargs when a function should accept any number of named arguments.

def student_details(**kwargs):    
    print(kwargs)
    
student_details(name="Ali", age=20, city="Hyderabad")


#- kwargs is a dictionary inside the function.
#- Each keyword becomes a dictionary key, and its value is stored against that key.


#Feature	             *args	                 **kwargs

#Accepts	    Extra positional arguments	Extra keyword arguments
#Stored as	             Tuple	                  Dictionary
#Example	          func(10, 20)	           func(name="Ali")

#5. Lambda functions

#A lambda function is a small anonymous function created using the lambda keyword.

#It can contain only a single expression, whose result is returned automatically.


#Normal function
def square(n):    
    return n * 2

print(square(5))
#Equivalent lambda function
square = lambda n: n * n
print(square(5))

# Syntax:

#lambda parameters: expression
#- lambda creates the function.
#- n is the parameter.
#- n * n is the expression.
#- The expression's result is returned automatically.


#Python's four main scope levels follow the LEGB rule:
#- L — Local: Inside the current function.
#- E — Enclosing: Inside an outer function that contains another function.
#- G — Global: Defined at the module level, outside functions.
#- B — Built-in: Names Python provides, such as print(), len() and sum().


count = 10

def update():
    count = 20
    print("Inside:", count)

update()
print("Outside:", count)

