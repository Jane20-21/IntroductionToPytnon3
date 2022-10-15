# Наибольший общий делитель. В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел.
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки.
# Входные данные
# 36
# 12
# 144
# 18
# Выходные данные
# 6


from functools import reduce
ist = [36, 12, 144, 18]
print(ist)

try:
    from math import gcd
except ImportError:
    from fractions import gcd
print(reduce(gcd, ist))
