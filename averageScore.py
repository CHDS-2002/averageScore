# os - библиотека для работы с консолью
# math - библиотека для работы с математическими функциями
# numpy - библиотека для работы с математическими объектами
# statistics - библиотека для работы со статистическими данными

import os
import math
import numpy
import statistics

# Зададим цвет шрифта консоли
os.system('COLOR B')


def summary(values):
    summ = 0  # summ - сумма

    for i in range(len(values)):
        summ += values[i]  # Формуруем сумму

    return summ  # Возвращаем сумму


def meaning(values):
    return summary(values) / len(values)
    # Возвращаем среднее значение


grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
# grades - список оценок

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# students - список учеников

# Рассчитаем средний балл каждого ученика

# 1 способ - воспользуемся функциями sum и len
means = [sum(grades[i]) / len(grades[i]) for i in range(len(grades))]
# 2 способ - воспользуемся сформированной функцией meaning
means = [meaning(grades[i]) for i in range(len(grades))]
# 3 способ - воспользуемся функциями len и fsum библиотеки math
means = [math.fsum(grades[i]) / len(grades[i]) for i in range(len(grades))]
# 4 способ - воспользуемся функцией mean библиотеки numpy
means = [numpy.mean(grades[i]) for i in range(len(grades))]
# 5 способ - воспользуемся функцией mean библиотеки numpy
means = [statistics.mean(grades[i]) for i in range(len(grades))]

students = list(students)  # преобразовываем множество в список
students = sorted(students)  # сортируем по алфавиту список
info = {students[i]: means[i] for i in range(len(means))}
# формируем словарь info из списков students и means

# Выводим информацию об учениках
print('\nИНФОРМАЦИЯ ОБ УЧЕНИКАХ\n')
print(info, '.\n')

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли
