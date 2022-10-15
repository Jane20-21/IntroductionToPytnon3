# Задача Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ), применив лямбды,
# filter, map, zip, enumerate, списочные выражения.

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

n = str(input('Вредите вещественное число: '))

# Было решение:
#sum = 0
# for i in range(len(n)):
#    if n[i].isdigit():
#        sum += int(n[i])
# print(sum)

# Новое решение:
lst = list(map(int, filter(lambda x: x.isdigit(), n)))
sum = sum(lst, start=0)
print(sum)