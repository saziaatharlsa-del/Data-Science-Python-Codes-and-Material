a = 10
b = 0

print(a / b)
print("Program completed")

a = 10
b = 0

try:
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

print("Program completed")

try:
    number = int("hello")
    print(number)
except ValueError:
    print("Invalid number")
print("Finished")



try:
    a = int(input("Enter the numerator: "))
    b = int(input("Enter the denominator: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Please enter a denominator other than zero.")


except ValueError:
    print("Please enter valid numbers.")

#--------------------------------------------------------

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Please enter valid integers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Division successful!")
    print("Result:", result)

finally:
    print("Program execution finished.")


#possible inputs

10, 2
10, 0
hello