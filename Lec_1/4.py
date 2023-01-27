# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

a = 1 > 4
print(a) # False

a = 1 < 4 and 5 > 2
print(a) # True

a = 1 == 2
print(a) # False операция сравнения

a = 1 != 2
print(a) # True операция неравенства

a = 'qwe'
b = 'qwe'
print(a == b) # True 

a = [1, 2]
b = [1, 2]
print(a == b) # True 

a = 1 < 3 < 5
print(a) # True 

func = 1
T = 4
x = 2
print(func < T > x) # True, тройное неравенство

f = 1 > 2 or 4 < 6
print(f) # True, хотя бы одно высказывание истина

k = [1, 2, 3, 4]
print(k)       # [1, 2, 3, 4]
print(not 2 in k)  # False, 2 содержится в этом списке 

is_odd = k[0] % 2 == 0  # факт четности числа
print(is_odd)           # False

# По умолчанию в Python 0 - ложь, 1 - истина
is_odd = not k[0] % 2
print(is_odd)   # False
# Получим тоже самое что и в предыдущем задании, но более Python вариант
