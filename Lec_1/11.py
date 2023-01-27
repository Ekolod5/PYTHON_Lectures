# Списки
# Списки - пронумерованная, изменяемая коллекция объектов

numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]

numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]

ran = range(1, 6)
print(type(ran))     # <class 'range'>
numbers = list(ran)  
print(type(numbers)) # <class 'list'>

numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]

print(f'{len(numbers)} len') # 5 len - в нашем списке 5 элементов

for i in numbers:
   i *= 2
   print(i)     # 20 4 6 8 10
print(numbers)  # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']

for e in colors:
   print(e)     # red, green, blue

for e in colors:
   print(e*2)     # redred, greengreen, blueblue

colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True

colors.remove('red') # del colors[0] удалить элемент
