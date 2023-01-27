# Типы данных и переменная
# int, float, boolean, str, list, None

value = None
print(type(value))

a = 123
b = 1.23
print(type(a)) # <class 'int'>
print(type(b))

value = 1234
print(type(value))

s = 'hello world'
print(s) # вывод строки

k = "hello \ ' world"
print(k) # вывод строки

p = "hello \nworld"
print(p) # \n перенести на новую строку

print(a, b, s) 
print(a, '-', b, '-', s)                 # 123 - 1.23 - hello world
print('{} - {} - {}'.format(a, b, s))    # 123 - 1.23 - hello world
print(f'{a} - {b} - {s}') # интерполяция - 123 - 1.23 - hello world 

print('{1} - {2} - {0}'.format(a, b, s)) # 1.23 - hello world - 123

f = True # False
print(f)

list = []
print(list)

list = [1, 2, 3]
print(list)

list = ['1', '2', '3', 'hellow'] # строковый тип данных
print(list)

list = ['1', '2', '3', 'hellow', 1, 2] # можем миксовать тип данных строковый и целечисл.
print(list)
