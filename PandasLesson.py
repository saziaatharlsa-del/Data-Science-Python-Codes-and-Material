#Data analysis and manipulation

#Pandas is a Python library used to organize, clean, filter, analyze, 
# and summarize data in tables.

#A Series is a one-dimensional labeled collection of values.

import pandas as pd

marks = pd.Series([85, 72, 90, 45, 68])

print(marks)

#Creating a Series with custom labels

marks = pd.Series([85, 72, 90],index=["Asha", "Rahul", "Sara"])
print(marks)

print(marks["Asha"])

#A Pandas DataFrame is similar to a table in Excel or a 
# database, with rows and columns.

#import pandas as pd — imports Pandas.

#pd.DataFrame(data) — creates a table from the data.

#print(df) — displays the table.

#data-The dictionary containing the original data.

#df - A variable that stores the DataFrame — 
# our table of data.

#0, 1, 2 - The row index labels Pandas assigns 
# automatically by default.

#Select one column

print(df["Name"])

#Select multiple columns

print(df[["Name", "Marks"]])

#A DataFrame is a two-dimensional, labeled data structure with rows and columns. 

import pandas as pd

data = {
    "Name": ["Asha", "Rahul", "Sara", "John", "Meera"],
    "Age": [20, 21, 20, 22, 21],
    "City": [
        "Hyderabad",
        "Chennai",
        "Hyderabad",
        "Bengaluru",
        "Chennai"
    ],
    "Marks": [85, 45, 92, 67, 38]
}

df = pd.DataFrame(data)

print(df)

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())

#df.head()	Displays the first five rows by default
#df.tail()	Displays the last five rows by default
#df.shape	Returns the number of rows and columns
#df.columns	Displays column labels
#df.dtypes	Displays the data type of each column
#df.info()	Summarizes columns, non-null counts, and data types
#df.describe()	Summarizes numerical columns statistically

df["Marks"]       # Selects a column
df.iloc[0]        # Selects the first row by position
df.iloc[0, 3]     # Selects the first row, fourth column

#iloc — position-based selection

print(df.iloc[0])
print(df.iloc[0:3])
print(df.iloc[1, 3])

df.iloc[0]     #selects the first row.
df.iloc[0:3]   #selects the first three rows.
df.iloc[1, 3]  #selects the value at the second row and fourth column: 45.

#loc — label-based selection
data = {
    "Name": ["Asha", "Rahul", "Meera", "Ali"],
    "Marks": [85, 90, 78, 92],
    "Course": ["Python", "Data Science", "Python", "AI"]
}

df = pd.DataFrame(data, index=["S1", "S2", "S3", "S4"])

print(df)

print(df.loc["S2"])

#- loc selects using labels, whereas iloc selects using 
# integer positions.

#Sorting data
#Sort by marks in ascending order

print(df.sort_values("Marks"))

#Sort from highest to lowest
print(df.sort_values("Marks", ascending=False))

#- sort_values() sorts according to column values.
#- ascending=True sorts from smaller to larger.
#- ascending=False sorts from larger to smaller.

#By default, these operations return a sorted DataFrame without modifying the original one.

#To retain the sorted result, assign it back:

df = df.sort_values("Marks", ascending=False)

#Statistical analysis
print("Average:", df["Marks"].mean())
print("Total:", df["Marks"].sum())
print("Highest:", df["Marks"].max())
print("Lowest:", df["Marks"].min())
print("Count:", df["Marks"].count())
print("Median:", df["Marks"].median())

#- count() — number of non-missing values.
#- sum() — sum of the values.
#- mean() — arithmetic average.
#- median() — middle value after ordering the observations.



data = {
    "Name": ["Asha", "Rahul", "Sara", "John", "Meera"],
    "Age": [20, 21, 20, 22, 21],
    "City": [
        "Hyderabad",
        "Chennai",
        "Hyderabad",
        "Bengaluru",
        "Chennai"
    ],
    "Marks": [85, 45, 92, 67, 38]
}


#Count students by city
print(df["City"].value_counts())

#This counts the occurrences of each city in the dataset.

#Calculate average marks by city
print(df.groupby("City")["Marks"].mean())

#1. groupby("City") groups students by city.
#2. ["Marks"] selects the marks within each group.
#3. .mean() calculates the average for each group.

#This introduces one of Pandas' most valuable analytical features: grouping data and summarizing it.

#Handling missing values

import pandas as pd
data = {"Name": ["Asha", "Rahul", "Sara", "John"],
        "Marks": [85, None, 92, 67],
        "Age": [20, 21, None, 22]}
df = pd.DataFrame(data)
print(df)

#None represents a missing value here, which Pandas generally represents as NaN in these numeric columns.
#Identify missing values

print(df.isnull())
print(df.isnull().sum())

#The second command counts missing values in each column.

#Remove rows containing missing values
clean_df = df.dropna()
print(clean_df)

#dropna() returns a DataFrame with rows containing missing values removed, by default.


#Fill missing marks with the average
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)

#fillna() replaces missing values with the specified value.

import pandas as pd

data = {
    "Name": ["Asha", "Rahul", "Meera", "Ali"],
    "Marks": [85, 90, 78, 92],
    "Course": ["Python", "Data Science", "Python", "AI"]
}

df = pd.DataFrame(data)

print(df)

#Filtering rows using conditions

import pandas as pd

data = {
    "Name": ["Asha", "Rahul", "Meera", "Ali"],
    "Marks": [85, 90, 78, 92],
    "Course": ["Python", "Data Science", "Python", "AI"]
}

df = pd.DataFrame(data)

#Students who scored more than 80

print(df)

condition = df["Marks"] >= 80

print(condition)

result = df[condition]

print(result)

#condition stores the True/False results.

#df[condition] filters the DataFrame using those results.

#result contains only the matching students.

#Students enrolled in Python

print(df[df["Course"] == "Python"])

#Reading and writing CSV files

#A CSV file stores tabular data as text, with fields commonly separated by commas.

#Save this file in the same folder as the Python script.

#Read the CSV file

import pandas as pd
df = pd.read_csv("students.csv")
print(df)

#read_csv() loads the CSV data into a DataFrame.

#Save the DataFrame to a new CSV file

df.to_csv("student_report.csv", index=False)

#- to_csv() writes a DataFrame to a CSV file.
#- "student_report.csv" is the output filename.
#- index=False prevents Pandas from adding the DataFrame index as an extra column.

#Filtering data using conditions

passed = df[df["Marks"] >= 50]
print(passed)

#df["Marks"] >= 50 produces a Boolean Series.
#df[...] selects the rows where the condition is True.

result = df[
    (df["Marks"] >= 50) &
    (df["City"] == "Hyderabad")
]

print(result)

result = df[
    (df["Marks"] >= 80) |
    (df["City"] == "Chennai")
]

print(result)