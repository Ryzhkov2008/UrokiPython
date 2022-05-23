# Исключения и их обработка

# Деление на 0
# a = 100/0
# print(a)

# try:
#     a = 1/0
# except ZeroDivisionError:
#     a = 0
# print(a)

# a = 2 + "1"
# print(a)

# try:
#     b = 2 +"1"
# except:
#     print("Ошибка в коде")

# print(int("qwerty"))

# my_list = [1, 2, 3, 4, 5]
# try:
#     my_list[6]
# except IndexError:
#     print("Этого индекса нет в списке")


# Оператор finally выполняется в любом случае

# Задача 3
# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# try:
#     c = a/b
# except ZeroDivisionError:
#     print("что-то пошло не так")
# else:
#     print("Результат в квадрате:", c ** 2)
# finally:
#     print("конец")

# Задача 4


d = {1:2, 3:4}
d.update({5:6})
print(d)




