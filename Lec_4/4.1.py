# 1
def f(x):
    return x * x
print(f(5))     # 25
print(type(f))  # <class 'function'>

a = f
print(type(f))  # <class 'function'>
print(a(5))  # 25


# 2
def calk1(a):
    return a + a

def calk2(a):
    return a * a

def math(op, x):
    print(op(x))

math(calk1, 5)   # 10
math(calk2, 5)   # 25


# 3
def calk1(a, b):
    return a + b

def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(calk1, 5, 45)   # 50
math(calk2, 5, 45)   # 225


# 4. Анонимные, lambda-функции

def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

# def calk1(a, b):
#     return a + b

calk1 = lambda a, b: a + b

math(calk1, 5, 45)   # 50
math(calk2, 5, 45)   # 225


# 5

def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(lambda a, b: a + b, 5, 45)   # 50


# 6. В списке хранятся числа. Нужно выбрать только чётные числа и 
# составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38 
# Получить: [(2, 4), (8, 64), (38, 1444)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = list()

for i in data:
    if i % 2 == 0:
        res.append((i, i**2))

print(res)


# 7. В списке хранятся числа. Нужно выбрать только чётные числа и 
# составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38 
# Получить: [(2, 4), (8, 64), (38, 1444)]

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)                   # [1, 2, 3, 5, 8, 15, 23, 38]
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)                                # [2, 8, 38]
res = list(select(lambda x: (x, x**2), res))
print(res)                                # [(2, 4), (8, 64), (38, 1444)]
