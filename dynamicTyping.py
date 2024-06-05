# os - библиотека для работы с консолью
# random - библиотека для работы со случайными данными
# datetime - библиотека для работы с датами
# russian_names - библиотека для работы с данными
# русских людей

import os
import random
import datetime
import russian_names

# Зададим цвет шрифта консоли - голубой
os.system('COLOR B')


# Создадим класс Human
# Name - имя
# Age - возраст
# Is_Student - статус студента
class Human:
    def __init__(self, name, age, is_student):
        self.Name = name
        self.Age = age
        self.Is_Student = is_student


NAME = russian_names.RussianNames().get_person().split()[0]
# NAME - имя
BIRTH_YEAR = 2002  # BIRTH_YEAR - год рождения
CURRENT_YEAR = datetime.datetime.now().year
# CURRENT_YEAR - текущий год
AGE = CURRENT_YEAR - BIRTH_YEAR  # AGE - возраст
IS_STUDENT = True  # IS_STUDENT - статус студента

LEFT = 1  # LEFT - левая граница
RIGHT = 5  # RIGHT - правая граница

# Создадим экземпляр human класса Human
human = Human(NAME, AGE, IS_STUDENT)

# Выведем информацию об экземпляре класса
print('\nИНФОРМАЦИЯ О ЧЕЛОВЕКЕ: \n')
print('Имя:', human.Name, end='.\n')
print('Возраст:', human.Age, end='.\n\n')

# Выведем новую информацию о человеке
print('ОБНОВЛЁННАЯ ИНФОРМАЦИЯ:\n')
print('Имя: ', human.Name, end='.\n')

# Зададим значение переменной new и выведем
# его на экран
new = random.randint(LEFT, RIGHT)
print('Изменение возраста:', new, end='.\n')

# Сложим new со значением Daniil.Age
# и выведем его на экран
human.Age += new
print('Новый возраст:', human.Age, end='.\n')

# Зададим значение переменной is_student
# и выведем его на экран
is_student = human.Is_Student
student = 'студент' if human.Is_Student else 'человек'
print('Статус:', student, end='.\n\n')

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли
