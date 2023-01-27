# Немного остроках
text = 'съешь еще этих мягких французских булок'
print(len(text))                    # 39
print('еще' in text)                # True
print(text.isdigit())               # False
print(text.islower())               # True
print(text.replace('еще', 'ЕЩЕ'))   # замена текста 'еще' на 'ЕЩЕ'

for c in text:
   print(c)

# help(text.istitle)  # help встроенная справка
# help(str) 

print(text[0])               # с - выдаст первую букву строки
print(text[1])               # ъ - выдаст вторую букву строки
# print(text[len(text)])     # IndexError - выдаст ошибку, индексация с 0
print(text[len(text)-1])     # к - -1 - это первая буква с конца строки 
print(text[-5])              # б - -5 - это пятая буква с конца строки 
print(text[:])               # съешь еще этих мягких французских булок
# значит по умолчанию будет print(text[0:len(text)-1])  
print(text[:2])              # съ - от нулевого до второго символа
print(text[0:2])             # съ - от нулевого до второго символа
print(text[len(text)-2:])    # ок
print(text[2:9])             # ешь еще
print(text[6:-18])           # еще этих мягких
print(text[0:len(text):6])   # сеикакл
print(text[::6])             # сеикакл
text = text[2:9] + text[-5] + text[0:2] # ...
