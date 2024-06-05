# os - library for working with the console
# math - library for working with mathematical functions
# numpy - library for working with mathematical objects
# statistics - library for working with statistical data

import os
import math
import numpy
import statistics

# Setting the font color of the console
os.system('COLOR B')


def summary(values):
    summ = 0  # summ - sum

    for i in range(len(values)):
        summ += values[i]  # We form the amount

    return summ  # We are returning the amount


def meaning(values):
    return summary(values) / len(values)
    # Returning the average value


grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
# grades - list of ratings

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# students - list of students

# Let's calculate the average score of each student

# 1 the method is to use the sum and len functions
means = [sum(grades[i]) / len(grades[i]) for i in range(len(grades))]
# 2 the method is to use the generated meaning function
means = [meaning(grades[i]) for i in range(len(grades))]
# 3 the method is to use the len and fsum functions of the math library
means = [math.fsum(grades[i]) / len(grades[i]) for i in range(len(grades))]
# 4 the method is to use the mean function of the numpy library
means = [numpy.mean(grades[i]) for i in range(len(grades))]
# 5 the method is to use the mean function of the numpy library
means = [statistics.mean(grades[i]) for i in range(len(grades))]

students = list(students)  # converting a set to a list
students = sorted(students)  # let's sort the list alphabetically
info = {students[i]: means[i] for i in range(len(means))}
# creating an info dictionary from the lists of students and means

# We display information about the students
print('\nINFORMATION ABOUT STUDENTS\n')
print(info, '.\n')

try:
    os.system('PAUSE')  # Stopping the program
    os.system('CLS')  # Clearing the console screen
except:
    os.system('CLS')  # Clearing the console screen
