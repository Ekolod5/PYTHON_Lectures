# Функции
# Функция — это фрагмент программы, используемый многократно.

# def function_name(x):
     # body line 1
             # ...
     # body line n
     # optional return

# Задача. Необходимо создать функцию sumNumbers(n), 
# которая будет считать сумму всех элементов от 1 до n.
# 1. Необходимо создать функцию:
# def sumNumbers(n):
# Очень важно понимать одну вещь, сколько аргументов мы передаем, столько и принимаем. 
# Или наоборот сколько аргументов мы принимаем, столько и передаем. 
# В нашем случае функция sumNumbers принимает 1 аргумент(n).

def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    print(summa)
sum_numbers(5)        # 15


def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
print(sum_numbers(4))  # 10


def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
a = sum_numbers(5)
print(a)               # 15


def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
    print('stop')  # не подсвечивает и не распечатывает
a = sum_numbers(6)
print(a)  

def sum_numbers(n, y = 'Hello'): # передаем два аргумента n, y
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
    print('stop')  # не подсвечивает и не распечатывает
a = sum_numbers(5)
print(a)  
# Hello
# 15


def sum_str(*args): # можно передавать неограниченное кол-ко переменных
    res = ''
    for i in args:
        res += i
    return res
print(sum_str('q', 'e', 'l'))  # qel
print(sum_str('q', 'e', 'l', 'r', 'f'))  # qelrf


def sum_numbers(n, y = 'Hello'): # передаем два аргумента n, y
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
    print('stop')  # не подсвечивает и не распечатывает
a = sum_numbers(5)
print(a, 'qwerty')  
# Hello
# 15 qwerty
