#Напишите программу, которая будет запрашивать на вход числа (через запятую на одной строке)
# и выводить наибольшее значение из списка.
#l = list(map(int, input().split(',')))
#m = l[0]
#print([(m := i) for i in l if i > m][-1])
l = list(map(int, input().split(',')))
m = l[0]
for i in l:
    if i > m:
        (m := i)
print(m)

# 2.1
l = int(input('Vvedi 0'))
m = 0
while l != 0:
  m += l
  l=int(input('Vvedi 0:'))
print(l)
print('summ:', m)

# 2.2Напишите программу, которая будет запрашивать на вход числа (каждое с новой строки) до тех пор,
# пока не будет введен ноль (0). На выход должно выводиться второе по величине значение.
l = int(input('Vvedi 0'))
m = []
while l != 0:
    m.append(l)
    l=int(input('Vvedi 0:'))
max = m[0]
for i in m:
    if i > max:
        (max := i)
        m.remove(max)
print('max:', max)

#3 Напишите программу, которая принимает на вход год, а на выход выдает количество дней в этом году.
year = int(input('Vvedi god'))
if year % 4 == 0:
    print('366')
else:
    print('365')

#4 Напишите программу, которая на вход получает число, а на выходе сообщает, простое это число или составное.
num = int(input('Vvedi num'))
i = 2
j = 0
for i in range(1,10):
    if num % i == 0:
        j+=1
    i+=1
if num == 1 or j<=2:
    print('Простое число')
else:
    print("Сложное число")
print(i,j)

#Напишите программу, которая на вход получает число, а на выходе сообщает, простое это число или составное.
num = int(input('Vvedi num'))
i = 2
j = 0
for i in range(1,10):
    if num % i == 0:
        j+=1
    i+=1
if num == 1 or j<=2:
    print('Простое число')
else:
    print("Сложное число")
print(i,j)

#6 Напишите программу, которая на вход получает целое число больше 2 и
# выводит по нему его наименьший натуральный делитель, отличный от 1
num = int(input('Vvedi num bolshe 2: '))
if num <= 2:
    num = int(input('Vvedi num bolshe 2: '))
i = 0
for i in range (2, num):
    if num%i == 0:
        print("наименьший натуральный делитель", i)
        break
print('Конец')

#7. Напишите программу, которая поможет составить план тренировок для подготовки к марафону.
# Она получает на вход число километров на планируемом марафоне, сколько пользователь планирует
# пробежать в первый день тренировок и на сколько процентов планирует увеличивать каждый день это расстояние.
# На выходе программа должна выдавать, сколько дней пользователю потребуется для того,
# чтобы подготовиться пробежать целевое количество километров.
distanse = int(input('Vvedi Distanse: '))
firts_try = int(input('firts_try: '))
increase = int(input('increase '))
increase = increase/100 + 1
i = 0
while firts_try < distanse:
    i+=1
    firts_try*=increase
print('Нужно заниматся дней: ', i)

#8. Напишите программу, которая на вход получает число n и считает по нему сумму 1²+2²+3²+...+n².
num = int(input('Vvedi num: '))
summ = 0
i = 0
while i != num:
    i += 1
    summ += i**2
print(summ)

#9. Напишите программу, которая на вход получает число n и считает по нему сумму сумму 1! + 2! + 3! + ... + n!
num = int(input('Vvedi num'))
summ = 0
res: int = 1
for i in range (1, num+1):
   res *= i
   summ += res
print(summ)

#10 Напишите программу, которая получает на вход последовательность чисел (каждое число с новой строки
# до того момента, пока пользователь не введет 0) и считает количество четных элементов в последовательности.
l = int(input('Vvedi 0'))
j = 0
while l != 0:
    l = int(input('Vvedi 0:'))
    if l%2 == 0:
        j+=1
print(j)

#11. Напишите программу, которая формирует список игроков женской команды по мини-футболу.
# Программа должна записывать возраст и пол претендента. Возраст должен запрашиваться после пола и только
# в том случае, если пол претендента женский. Если пол претендента мужской, программа должна сообщать о том,
# что он не подходит. Возраст претенденток должен быть от 18 до 35 лет. Если кандидат удовлетворяет требованиям,
# должно появляться соответствующее сообщение. Всего в команде могут быть только шесть человек.
# Когда необходимое число набирается, запись закрывается и выводится сообщение "Запись в команду закрыта".
team = []
while len(team) != 6:
    pol = str(input('Vvedi pol: '))
    if pol == 'мужской':
        print('Ты не подходишь')
    if pol == 'женский':
        age = int(input('Vvedi age: '))
        age1 = str(age)
        teammeit = pol+" "+age1
        team.append(teammeit)
        if age > 35 or 18 < age:
            print('Ты подходишь')
        else:
            print("ТЫ не подходишь по возрвсту")
            break
    else:
        print('Неверно введени данные')
    if len(team) == 6:
        print('Запись закрыта')
print(team)

#12. Напишите программу, которая на вход получает максимальную ширину ромба и рисует его.
# Гарантируется, что входное число всегда нечетное.
l = int(input('Vvedi l'))
i = 1
j = 0
if l%2 == 0:
    print('Введи четное число')
else:
    while i <= l:
        if i == l:
            print(l*'*')
            break
        else:
            print(" "*((l//2)-j) + "*" * i)
            i += 2
            j+=1
    while i >= 1:
        if i == 1:
            break
        else:
            i -= 2
            j -= 1
            print(" " * ((l // 2) - j) + "*" * i)

#13. Напишите программу, которая запрашивает у пользователя сторону квадрата и символ,
# а затем рисует этот символ по диагоналям квадрата. Гарантируется, что входное число всегда нечетное.
l = int(input('Vvedi l'))
simv = str(input('Vvedi simviol'))
i = 1
j =0
if l%2 == 0:
    print('Введи четное число')
else:
    while i <= l:
        if i == l:
            print('_'*(i//2)+simv+'_'*(i//2))
            i += 2
            j += 1
            break
        else:
            print(j * '_' + simv + (l-i-1)*'_' + simv + j*'_')
            i += 2
            j += 1
    while i > 1:
        if i == 1:
            print(simv*i + (l-2)*'_' + simv*i)
            i -= 2
            j -= 1
            break
        else:
            if i>l:
                i -= 2
                j -= 1
            else:
                i -= 2
                j -= 1
                print(j * '_' + simv + (l - i - 1) * '_' + simv + j * '_')

#14. В корзине лежат шары. Если разложить их в кучи по 2, останется один. Если разложить в кучи по 3, останется один.
# Если разложить в кучи по 4, останется один. Если разложить в кучи по 5, останется один. Если разложить в кучи по 6,
# останется один. Если разложить в кучи по 7, не будет остатка. Нужно найти минимальное количество шаров, удовлетворяющее условию.
for i in range(7,1000):
    if(all([i % 2 == 1, i % 3 == 1, i % 4 == 1, i % 5 == 1, i % 6 == 1, i % 7 == 0])):
        print(i)
        break

#15. Напишите программу, которая убирает из списка повторяющиеся элементы. Программа должна запрашивать на вход слова,
#каждое с новой строки, пока пользователь не введет пустую строку. Затем должна выводить список без повторяющихся элементов.
spisok = []
i = input('Vvedi ima')
while  i !='':
    if i not in spisok:
        spisok.append(i)
        i = input('Vvedi ima')
    else:
        i = input('Vvedi ima')
print(spisok)

#16. Напишите программу, которая выводит число пар одинаковых элементов в списке. При этом если два элемента
# образовали пару, они не могут вступить в пару с другими элементами. Программа должна запрашивать на вход слова,
# каждое с новой строки, пока пользователь не введет пустую строку.
spisok = []
i = input('Vvedi ima')
j = 0
while  i !='':
    if i in spisok:
        j+=1
        while i in spisok:
            spisok.remove(i)
    else:
        spisok.append(i)
    i = input('Vvedi ima')
print(j)

#Будем считать, что кубик может иметь неограниченное количество граней (натуральное число).
# Напишите программу, которая запрашивает, сколько граней имеется у двух разных кубиков.
# Затем выводит все возможные комбинации результатов бросков двух таких кубиков.
gran1 = int(input('Vvedi gran1: '))
gran2 = int(input('Vvedi gran2: '))
i = 0
if i <= gran1:
    while i < gran1:
        j=1
        i+=1
        while j <= gran2:
            print(i, j)
            j += 1