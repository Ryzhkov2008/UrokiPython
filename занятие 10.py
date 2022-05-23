# Занятие 10 кортежи
# a = (10, 2.13, "square", 89, 'C')
# print( a[2])

# a = (1,(1, 2, 3),"not")
# a[2][1] = 21
# print(a)

# c = ((1, 2, 5), [2,7,-100], "Python")
# print(type(c))


# name, age, company, position = ("Tom", 37, "Google", "software developer")
# print(name)         # Tom
# print(age)          # 37
# print(position)     # software developer
# print(company)     # Google

#Создайте кортеж из случайных 10 чисел.
# Найдите индексы максимального и
# минимального элемента

#print(a.index(min(a)),a.index(max(a)))


# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# a = sum(C_1)
# b = sum(C_2)
# if a>b:
#     print('Сумма больше в кортеже C_1:', a)
#     if b>a:
#         print('Сумма больше в кортеже C_2:', b)
# print('Мин индекс С_1:',d.index(min(C_1)),'Макс индекс С_1:',d.index(max(C_1)))
# print('Мин индекс С_2:',z.index(min(C_2)),'Макс индекс С_2:',z.index(max(C_2)))

import random
my_list = [random.randint(0, 10) for _ in range(10)]
print('Оригинальный список:', my_list)
answer = [(my_list[i_num], my_list[i_num + 1]) for i_num in range(0, len(my_list), 2)]
print('Новый список:', answer)


