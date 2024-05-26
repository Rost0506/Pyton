#1. Почему возникла ошибка? Объясните и исправьте.
# !!! f - локальная переменная, а был вызов глобальной
# def factorial(n):
#     f = 1
#     for i in range(2, n + 1):
#         f = f * i
#     return f
#
# factorial(3)
# print(f)
def factorial(n):
    f=1
    for i in range(2, n + 1):
        f = f * i
    return f

factorial(3)
print(factorial(3))

# 2. Почему переменная S после запуска функции сохранила значение ноль?
# S = 0 - !!! должна быть внутри функции
# def sum(n, m):
#     S = n + m
#     return S
#
# print(sum(3, 4))
# print(S) - это локальная, а не глобальная переменная
def sum(n, m):
    S = 0
    S = n + m
    return S

print(sum(3, 4))

# 3. Почему возникла ошибка? Объясните и исправьте, чтобы функция могла работать с данными на входе в примере с `res`.

# def mult(*, q, w, e, r, t, y): - звездочка не нужна
#     return q + w + e + r + t + y
# res = mult(1, 2, 3, 4, 5, 6)
def mult( q, w, e, r, t, y):
    return q + w + e + r + t + y
res = mult(1, 2, 3, 4, 5, 6)
print(res)

# Почему возникла ошибка? Объясните и исправьте, чтобы функция могла работать с данными на входе в примере.
# def power(a, s, *, d):
#     res = a ** s ** d
#     print(res)
#
# power(d=4, 5, 6)
def power(a, s, d): # После именованого параметра нельзя ставить позиционные
    res = a ** s ** d
    print(res)

power(2, 2, d=2)

# Почему возникла ошибка? Объясните и исправьте, чтобы функция могла работать с данными на входе в примере.
# def mult2(*args):
#     res = 1
#     for i in args:
#         res += i
#     return res
#
# List = [1, 2, 3, 4, 5, 6, 7]
# print(mult2(List)) !!! НУЖНО ДОБАВИТЬ * ПЕРЕД LIST

def mult2(*args):
    res = 1
    for i in args:
        res += i
    return res

List = [1, 2, 3, 4, 5, 6, 7]
print(mult2(*List))

# Почему возникла ошибка? Объясните и исправьте
# def some_function(a, b, **kwargs, *args):
#     pass

def some_function(a, b,*args, **kwargs): # args всегда перед kwargs
    pass

# Почему не был создан новый список при повторном запуске функции? Объясните и исправьте.
# def to_buy(*new_items, shopping_list = []): !!! Так делать нельзя, нужно использовать None
#     for i in new_items:
#         shopping_list.append(i)
#     return shopping_list
#
# monday = to_buy('яблоки', 'молоко', 'хлеб')
# print(monday)
#
# tuesday = to_buy('груши', 'йогурт', 'мясо')
# print(tuesday)

def to_buy(*new_items, shopping_list = None):
    if shopping_list is None:
        shopping_list =[]
    for i in new_items:
        shopping_list.append(i)
    return shopping_list

monday = to_buy('яблоки', 'молоко', 'хлеб')
print(monday)

tuesday = to_buy('груши', 'йогурт', 'мясо')
print(tuesday)

# 8. Измените данную функцию так, чтобы она распечатывала названия продуктов из словаря в примере.
# def print_all(*kwargs):
#     for i in kwargs():
#         print(i)
#
# print_all(*{'1': 'яблоки', '2': 'молоко', '3': 'хлеб', '4': 'груши', '5': 'йогурт', '6': 'мясо'})

def print_all(**kwargs): # Для словарей нужно **
    for key, value in kwargs.items():
        print(value) # Выдаст значение

print_all(**{'1': 'яблоки', '2': 'молоко', '3': 'хлеб', '4': 'груши', '5': 'йогурт', '6': 'мясо'}) # Для словарей нужно **

# Программисты договорились, что переменные такого рода являются.. *(вопрос из лекции)*
# TOKEN = Ответ - Это константы

# Напишите функцию, которая с помощью рекурсии считает сумму последовательности с шагом m.
# В качестве аргументов подаются целые положительные числа n (последний элемент последовательности) и
# m (шаг последовательности). Считается, что все члены последовательности являются целыми положительными числами.
def sum_of_seq(n,m):
    if n<m:
        return n
    if n==1:
        return 1
    else:
        if m == 1:
            return (n + sum_of_seq(n=n - 1, m=m))
        else:
            return (n + sum_of_seq(n=n - m, m=m))

res = sum_of_seq(8,2)
print(res)

#Напишите функцию, которая возводит число в положительную степень с помощью рекурсии.
# В качестве аргументов подаются целые положительные числа n (число) и m (степень).
def sum_of_seq(n,m):
    if m == 0:
        return 1
    else:
        return (n * sum_of_seq(n=n, m=m-1))

res = sum_of_seq(2,3)
print(res)

#Напишите функцию, которая возводит число в отрицательную степень число с помощью рекурсии.
#В качестве аргументов подаются целое положительное число n (число) и целое отрицательное число m (степень).
def sum_of_seq(n,m):
    if m <= 1:
        return 1/n
    else:
        return (sum_of_seq(n=n*n, m=m-1))

res = sum_of_seq(3,1)
print(res)

#Напишите функцию, которая находит число Фиббоначи по его номеру.
# В качестве аргумента подается целое положительное число n (число).
