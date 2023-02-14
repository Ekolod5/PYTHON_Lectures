# Словари
# Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. 
# В словаре для определения элемента используется значение ключа (строка, число).

d = {}
d = dict()
d['q'] = 'qwerty'
print(d)          # {'q': 'qwerty'} если обратимся к крючку q будем получать qwerty

d['w'] = 'werty'
print(d)          # {'q': 'qwerty', 'w': 'werty'}
print(d['q'])     # qwerty

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 
print(dictionary)          # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'} 
print(dictionary['left'])  # ← типы ключей могут отличаться 
print(dictionary['up'])    # ↑ типы ключей могут отличаться dictionary['left'] = '⇐'
print(dictionary['left'])  # ⇐
# print(dictionary['type'])  # KeyError: 'type'
del dictionary['left']     # удаление элемента

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 
dictionary[895] = {}
print(dictionary)     # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→', 895: {}}


dictionary_1 = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 
del dictionary_1['left']     # удаление элемента
for item in dictionary_1:
    print('{}: {}'.format(item, dictionary_1[item]))
# Ответ up: ↑  
# down: ↓
# right: →


dictionary_2 = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 
del dictionary_2['left'] 
for item in dictionary_2:
    print(item)
# up
# down
# right


dictionary_3 = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 
del dictionary_3['left'] 
for (k, v) in dictionary_3.items():
    print(k, v)
# up ↑  
# down ↓
# right →

dictionary_4 = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 
print(dictionary_4.items())  # dict_items([('up', '↑'), ('left', '←'), ('down', '↓'), ('right', '→')])
for (k, v) in dictionary_4.items():
    print(k, v)
# up ↑
# left ←
# down ↓
# right →
