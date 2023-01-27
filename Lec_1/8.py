# Управляющие конструкции
# for

# for i in enumeration:
#      # operator 1
#      # operator 2
#      # ...
#      # operator n

# for i in 1, 2, 3, 4, 5:
#     print(i**2) # 1 4 9 16 25

# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i**2) # 1 4 9 16 25

# list = [1, 2, 3, 4, 10, 5]
# for i in list:
#     print(i) # 1 2 3 4 10 5

r = range(10)
for i in r:
    print(i) # получаем числа от 0 до 10
# 0 1 2 3 4 5 6 7 8 9

for i in range(5): # другой вариант
    print(i) # получаем числа от 0 до 5
# 0 1 2 3 4

for i in range(1, 5):
    print(i) # получаем числа от 1 до 5
# 1 2 3 4

for i in range(1, 10, 2):
    print(i) # получаем числа от 1 до 10, нечетные числа
# 1 3 5 7 9

for i in 'qwe - rty':
    print(i) # побуквенная разбивка
# q w e - r t y
