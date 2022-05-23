# №1
a = [1,2,3,4,5,3,2,2,5,7,8,9]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
     print(a[i], end='')

# №2
# my_list = [4, 6, 8, 9, 12, 5, 8, 9, 4]
# count = 0
# for i in range(len(my_list)):
#   for j in range(i+1, len(my_list)):
#     if my_list[i] == my_list[j]:
#       count+=1
# print(count)

# №3
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# s1 = sum(C_1)
# s2 = sum(C_2)
# if s1 > s2:
#   print("Сумма больше в кортеже C_1")
# else:
#   print("Сумма больше в кортеже C_2")
# minim_C_1, minim_C_2 = C_1.index(min(C_1)), C_2.index(min(C_2))
# maxim_C_1, maxim_C_2 = C_1.index(max(C_1)), C_2.index(max(C_2))
# print(f"Порядовые номера мин элементов, {minim_C_1}, {minim_C_2}",f "Порядковые номера мах элементов, {maxim_C_1}, {maxim_C_2}")
# print(f"порядковые номера минимальных элементов - {minim_C_1},{minim_C_2},", f"максимальных элементов - {maxim_C_1},{maxim_C_2}")

# №4
# text = 'An apple a day keeps the doctor away'
# d = {i:t.count(i) for i in t}
# print(d)

# №5
# menu = {"торт":["мука, сахар, масло, яйцо", 3, 2000],"мороженое":["молоко, сахар, яйцо, ванилин", 2, 1000],"фрукты":["фрукты", 1, 300]}
# d = ["состав", "цена", "вес", "вся информация"]
# product = input("Ведите название товара: -")
# if product in menu:
#   danno = input("состав, цена, вес или вся информация: -")
# else:
#   print("такого продукта нет в меню")
# if danno == d[0]:
#   print(f"в состав {product}а входит: {menu[product][0]}")
# elif danno == d[1]:
#   print(f"цена {product}а - {menu[product][1]} рубля за 100 г.")
# elif danno == d[2]:
#   print(f"в наличии {product}а - {menu[product][2]} грамм")
# elif danno == d[3]:
#   print(f"в состав {product}а входит: {menu[product][0]}, "
#  f"цена - {menu[product][1]} рубля за 100 г., в наличии - {menu[product][2]} грамм")
# while True:
#     good = input("Что вы выбрали?, n - ничего:")
#     if good == 'n' or good not in menu.keys():
#           break
#     gty = int(input("Введите количество товара:"))
#     if gty > menu[product][2]:
#         print("Количество не верно")
#         continue
#     if good in menu:
#         price = menu[good][1] * gty
#         a = menu[good][2] - gty
#         print("остаток товара",a)
#         print("цена :",price)

# №6
# my_list = [1, 2, 3 ,4, 5]
# my_list1 = [4, 6, 8, 9, 12, 5, 8, 9]
# a = len(my_list) + len(my_list1)
# print(a)

# №7
# k = int(input("input number: "))
# a = 0
# try:
#   a = 10 / k
# except ZeroDivisionError:
#   print('Деление на 0 недопустимо')
# print(a)
# finally:
#     print("Это всегда выполняется")

# №8
#  В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# баллов и посчитать средний балл по класс

while open("max.txt", encoding="utf-8") as file:






