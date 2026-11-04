#Numpy
#Numerical Python
#NumPy is a Python library used to work efficiently with numbers, arrays, matrices, 
#and mathematical operations.

numbers = [10, 20, 30, 40, 50]

import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)

print(type(numbers))

#An array is a collection of elements arranged in 
# one or more dimensions.

#A dimension tells us how data is organized. 
# 1D array is a sequence, 
# 2D array is a table, 
# 3D array is a collection of tables.

marks = np.array([80, 75, 90, 85])

marks = np.array([
    [80, 90],
    [75, 85],
    [90, 95]
])

marks = np.array([
    [
        [80, 90],
        [75, 85],
        [90, 95]
    ],
    [
        [70, 80],
        [85, 88],
        [92, 96]
    ]
])


import numpy as np

marks = np.array([85, 90, 78, 92])

print(marks)
print(marks.ndim)
print(marks.shape)

#np.array() creates a NumPy array.

#ndim tells us the number of dimensions. Here, it is 1.

#shape tells us how many elements are present along 
# each dimension. (4,) means four elements in one dimension.


#properties

#marks.ndim 
#marks.shape 
#marks.size
#marks.dtype


import numpy as np

marks = np.array([
    [[80, 85], [90, 75]],
    [[88, 91], [84, 95]]
])

print(marks)
print(marks.ndim)
print(marks.shape)


import numpy as np

sun = np.zeros(5)

print(sun)

#By default, NumPy uses floating-point numbers, so the zeros appear as 0. instead of 0.

a = np.zeros(5, dtype=int)
print(a)


import numpy as np

arr = np.zeros((2, 3))

print(arr)


np.ones(shape)

arr = np.ones((3, 2), dtype=int)
print(arr)

#np.arange(start, stop, step)

import numpy as np

sun = np.arange(5)

print(sun)


import numpy as np

sun = np.arange(2, 11, 2)

print(sun)


import numpy as np

sun = np.array([[10, 20, 30],
                [40, 50, 60]])

print("Array:")
print(sun)

print("Dimensions:", sun.ndim)
print("Shape:", sun.shape)
print("Total elements:", sun.size)
print("Data type:", sun.dtype)


#indexing

import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[0])
print(a[2])
print(a[4])



import numpy as np

marks = np.array([
    [85, 90, 78],
    [88, 92, 95]
])

print(marks[0, 0])
print(marks[0, 2])
print(marks[1, 1])


#slicing

a = np.array([10, 20, 30, 40, 50])

print(a[:3])
print(a[2:])
print(a[:])

import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(a[0:2, 0:2])


import numpy as np

print(np.zeros(5))
print(np.ones(4))
print(np.arange(1, 11))
print(np.arange(2, 11, 2))
print(np.arange(2, 13, 2).reshape(2, 3))
print(np.full(3, 7))
print(np.full((2, 3), 7))


#np.zeros(5) creates five zeros.
#np.ones(4) creates four ones.
#np.arange(1, 11) generates values from 1 up to, but not including, 11.
#np.arange(2, 11, 2) generates values starting at 2, increasing by 2, and stopping before 11.
#np.full(3, 7) creates three elements, each with the value 7


import numpy as np

# Create two NumPy arrays
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

print("Array A:", a)
print("Array B:", b)

# 1. Addition
print("\nAddition:", a + b)

# 2. Subtraction
print("Subtraction:", a - b)

# 3. Multiplication (element-wise)
print("Multiplication:", a * b)

# 4. Division
print("Division:", a / b)

# 5. Floor division (quotient without decimal part)
print("Floor Division:", a // b)

# 6. Modulus (remainder)
print("Modulus:", a % b)

# 7. Exponentiation (power)
print("Power:", a ** 2)

# 8. Square root
print("Square Root:", np.sqrt(a))

# 9. Square
print("Square:", np.square(a))

# 10. Absolute value
values = np.array([-10, -20, 30, -40, 50])
print("Absolute Value:", np.abs(values))

# 11. Exponential (e raised to each element)
small_values = np.array([1, 2, 3])
print("Exponential:", np.exp(small_values))

# 12. Natural logarithm
print("Natural Log:", np.log(a))

# 13. Logarithm base 10
print("Log Base 10:", np.log10(a))

# 14. Rounding decimal values
decimals = np.array([10.25, 20.56, 30.78])
print("Rounded:", np.round(decimals))

# 15. Ceiling (round up)
print("Ceiling:", np.ceil(decimals))

# 16. Floor (round down)
print("Floor:", np.floor(decimals))

# 17. Sum of elements
print("Sum:", np.sum(a))

# 18. Minimum value
print("Minimum:", np.min(a))

# 19. Maximum value
print("Maximum:", np.max(a))

# 20. Mean (average)
print("Mean:", np.mean(a))

# 21. Median
print("Median:", np.median(a))
#Median is the middle value when the data is arranged in ascending order.


# 22. Cumulative sum
print("Cumulative Sum:", np.cumsum(a))

# 23. Cumulative product
print("Cumulative Product:", np.cumprod(a))


# Variance

#Variance measures how far values are spread out from their mean.
print("Variance:", np.var(a))

#Step 1: Find the difference between each value and the mean.
#Step 2: Square each difference. Squaring makes all the differences non-negative.
#Step 3: Add the squared differences.

#Standard deviation

print("Standard Deviation:", np.std(a))


#Standard deviation — Typical spread around the mean
#Standard deviation is closely related to variance.
#Standard deviation is the square root of variance.

import numpy as np

group_a = np.array([48, 49, 50, 51, 52])
group_b = np.array([10, 30, 50, 70, 90])

print("Group A Mean:", np.mean(group_a))
print("Group A Variance:", np.var(group_a))
print("Group A Standard Deviation:", np.std(group_a))

print()

print("Group B Mean:", np.mean(group_b))
print("Group B Variance:", np.var(group_b))
print("Group B Standard Deviation:", np.std(group_b))