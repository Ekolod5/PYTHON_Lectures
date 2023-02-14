# Множества
# Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# Одно множество может содержать значения любых типов. 
# Если у Вас есть два множества, Вы можете совершать над ними любые стандартные 
# операции, например, объединение, пересечение и разность. 

# Чтобы упорядочить нужно создать списки

colors = {'red', 'green', 'blue'} 
print(colors)                      # {'red', 'green', 'blue'} 
colors.add('red')
print(colors)                      # {'red', 'green', 'blue'} 
colors.add('gray')                 # добавить
print(colors)                      # {'blue', 'green', 'gray', 'red'} gray - добавляет куда угодно
colors.remove('red')               # удалить


print(colors)                      # {'green', 'blue','gray'} 
# colors.remove('red')             # KeyError: 'red' colors.discard('red') # ok
colors.discard('red')              # ok 
# Проверяет значение red, есть ли оно в множестве.
# Если есть удаляет, если нет, то просто пропускает строку
print(colors)                      # {'green', 'blue','gray'} 

colors.clear()                     # удалить все значения из списка
print(colors)                      # set() - множество set


q = set()                          # можно создать множество

# Операции со множествами в Python:

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}

c = a.copy()
print(c)                             # {1, 2, 3, 5, 8}

u = a.union(b)
print(u)                             # {1, 2, 3, 5, 8, 13, 21}

i = a.intersection(b)                # пересечение элементов в обоих множествах
print(i)                             # {8, 2, 5}

dl = a.difference(b)                 # разность множест
print(dl)                             # {1, 3}

dr = b.difference(a)                 # разность множеств
print(dr)                            # {13, 21}

q = a.union(b).difference(a.intersection(b))
print(q)                              # {1, 21, 3, 13}


# Неизменяемое или замороженное множество(frozenset) — множество, 
# с которым не будут работать методы удаления и добавления.
a = {1, 2, 3, 5, 8}
b = frozenset(a)      # хоти заморозить множество a, т.е. мы не можем его изменять
print(b)              # frozenset({1, 2, 3, 5, 8})
