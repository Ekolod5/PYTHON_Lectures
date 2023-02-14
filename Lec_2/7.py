# Профилирование и отладка
# Самые распространенные ошибки:

# SyntaxError(Синтаксическая ошибка)
# number_first = 5
# number_second = 7
# if number_first > number_second # Отсутствие знака : Выдает ошибку!!!!
#     print(number_first)

# IndentationError(Ошибка отступов) 
# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first) # !!!!! # Отсутствие отступов

# TypeError(Типовая ошибка) 
# text = 'Python'
# number = 5   
# print(text + number)
# Нельзя складывать строки и числа
# Чтобы исправить нужно к 5 поставить кавычки '5'

# ZeroDivisionError(Деление на 0) 
# number_first = 5
# number_second = 0
# print(number_first // number_second)
# Делить на 0 нельзя

# KeyError(Ошибка ключа)
# dictionary = {1: 'Monday', 2: 'Tuesday'} 
# print(dictionary[3])
# Такого ключа не существует
 
# NameError(Ошибка имени переменной) 
# name = 'Ivan'
# print(names)
# Переменной names не существует

# ValueError(Ошибка значения) 
# text = 'Python'  # нужно ввести числа '555'
# print(int(text))
# Нельзя символы перевести в целые значения
 