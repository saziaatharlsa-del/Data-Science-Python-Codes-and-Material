#For loop

for i in range(1, 6):
    print(i)

a = "python"

b= [1,2,3,4]


#How does it work?
#1. The loop takes an item from a sequence.
#2. It executes the statements for that item.
#3. It moves to the next item.
#4. This continues until all items have been processed.
#5. The loop ends automatically when no items remain.


#While loop

i = 1
while i <= 5:
    print(i)
    i = i + 1


#How does it work?
#1. Python checks the condition.
#2. If the condition is true, the loop body executes.
#3. After execution, Python checks the condition again.
#4. If the condition is still true, the statements execute again.
#5. When the condition becomes false, the loop stops.


for i in range(1, 4):    
    print("Hello")


# Iteration	  Value of i	    Output
#    1	         1	            Hello
#    2	         2	            Hello
#    3	         3	            Hello


for i in range(1, 6):    
    print("Hello", i)


#Print numbers with their squares

for i in range(1, 6):    
    print(i, "Square =", i * i)

#Add numbers one by one

#Accumulation

total = 0
for i in range(1, 6):
    total = total + i

print("Total:", total)


# Iteration	    i	 total before addition	 total after addition
#    1	        1	        0	                        1
#    2	        2	        1	                        3
#    3	        3	        3	                        6
#    4	        4	        6	                        10
#    5	        5	        10	                        15


#Count how many even numbers are present

count = 0
for i in range(1, 11):    
    if i % 2 == 0:        
        count = count + 1

print("Even numbers count:", count)


#Print a pattern
for i in range(1, 6):    
    print("*" * i)


#While Loop

#1 Initialization — where the variable starts.

i = 1

#2 Condition — when the loop should continue.

while i <= 5:

#3 Update — how the variable changes.

i = i + 1


#Print numbers from 2 to 10, skipping by 2

i = 2
while i <= 10:    
    print(i)    
    i = i + 2



#Calculate the total of numbers entered by a user

#A shopkeeper enters the prices of three products and wants their total.

total = 0
count = 1
while count <= 3:    
    price = int(input("Enter product price: "))    
    total = total + price    
    count = count + 1
    
print("Total price:", total)


#Guess a number

secret = 7
guess = 0
while guess != secret:    
    guess = int(input("Guess the number: "))
print("Correct guess!")



#Find the sum of digits
number = 1234
total = 0
while number > 0:    
    digit = number % 10    
    total = total + digit    
    number = number // 10
print("Sum of digits:", total)


Step    number	  number % 10	 New total	   New number
1	     1234	     4	            4	           123
2	     123	     3	            7	           12
3	     12	         2	            9	           1
4	     1	         1	            10	           0


#break and continue

#Stop the loop at 4
for i in range(1, 8):    
    if i == 4:        
        break    
    print(i)


#Skip the number 4
for i in range(1, 8):    
    if i == 4:        
        continue    
    print(i)


#continue skips the remaining statements in the current iteration and moves to the next iteration.

#- break = stop the entire loop.
#- continue = skip one iteration.


#Q1. Write a Python program to print all numbers between 1 and 100 that are 
# divisible by both 3 and 5.

#Q2. Write a Python program to count how many digits are present in a 
# number without converting the number into a string.

#Q3. Write a Python program to display the multiplication table of a 
# number entered by the user, from 1 to 20.