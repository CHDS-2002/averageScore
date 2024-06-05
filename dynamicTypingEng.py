# os - library for working with the console
# names - library for working with names
# random - library for working with random data
# datetime - library for working with dates

import os
import names
import random
import datetime

# Let's set the font color of the console - blue
os.system('COLOR B')


# Let's create the Human class
# Name - name
# Age - age
# Is_Student - student status
class Human:
    def __init__(self, name, age, is_student):
        self.Name = name
        self.Age = age
        self.Is_Student = is_student


NAME = names.get_first_name()  # NAME - name
BIRTH_YEAR = 2002  # BIRTH_YEAR - birth year
CURRENT_YEAR = datetime.datetime.now().year
# CURRENT_YEAR - current year
AGE = CURRENT_YEAR - BIRTH_YEAR  # AGE - age
IS_STUDENT = True  # IS_STUDENT - student status

LEFT = 1  # LEFT - the left board
RIGHT = 5  # RIGHT - the right board

# Creating an instance human of the Human class
human = Human(NAME, AGE, IS_STUDENT)

# Let's get information about the person
print('\nINFORMATION ABOUT HUMAN: \n')
print('Name:', human.Name, end='.\n')
print('Age:', human.Age, end='.\n\n')

# Let's get new information about the person
print('NEW INFORMATION:\n')
print('Name: ', human.Name, end='.\n')

# Set the value of the new variable and
# display it on the screen
new = random.randint(LEFT, RIGHT)
print('Age change:', new, end='.\n')

# Add new with value Daniil.Age
# and output his on the screen
human.Age += new
print('A new age:', human.Age, end='.\n')

# Add the new value to the Daniil.Age value
# and display it on the screen
is_student = human.Is_Student
student = 'student' if human.Is_Student else 'human'
print('Status:', student, end='.\n\n')

try:
    os.system('PAUSE')  # Stopping the program
    os.system('CLS')  # Clearing the console screen
except:
    os.system('CLS')  # Clearing the console screen
