# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных
# друг другу.
# Считается, что любые два элемента, равные друг другу
# образуют одну пару,
# которую необходимо посчитать.

# numbers = [1, 3, 4, 5, 6, 7, 8, 3, 3, 1, 8, 8, 1, 1, 1]
# num_count = {}
# for num in numbers:
#     num_count[num] = numbers.count(num)
# pair_count = 0
# for value in num_count.values():
#     if value//2 >= 1:
#         pair_count += (value//2)
# print(pair_count)

# интересная реализаци Романа
# lst = [1,2,3,1,1,1,1,2,3,2, 2]
# print(lst)
#
# s = set(lst)
# without_pairs = 0
#
# for i in s:
#     if int(lst.count(i)) % 2 != 0:
#         without_pairs += 1
#
# print('В списке', int((len(lst) - without_pairs) / 2), 'парных элементов')

# Создайте словарь из строки ' An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите символы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку.

# phrase = ' An apple a day keeps the doctor away'
# letters_count = {letter: phrase.count(letter) for letter in phrase}
# print(letters_count)

# Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов
# продукции, а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и
# т.д.). Значение – список, который содержит состав, цену (за 100гр) и кол-во (в
# граммах).
# Предложите выбор:
# 1. Если человек хочет посмотреть описание: название – описание
# 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке:
# С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном
# списке
# 6. До свидания
#
# shop = {
#     'ice-cream': ['milk, sugar', 1, 10000],
#     'whiskey': ['alcohol', 10, 10000],
# }
# while True:
#     choice = input("""ЧЕГО ИЗВОЛИТЕ?
# название – описание: 1
# название – цена: 2
# название – количество: 3
# вся информация: 4
# приступить к покупке: 5
# до свидания: 6
# """)
#     if choice=='6':
#         break
#     elif choice=='1':
#         print('название – описание')
#         for k, v in shop.items():
#             print(f'{k} - {v[0]}')
#     elif choice=='2':
#         print('название – цена')
#         for k, v in shop.items():
#             print(f'{k} - {v[1]}')
#     elif choice=='3':
#         print('название – количество')
#         for k, v in shop.items():
#             print(f'{k} - {v[2]}')
#     elif choice=='4':
#         print('вся информация')
#         for k, v in shop.items():
#             print(k, '-', end=' ')
#             print(*v, sep=', ')
#     elif choice=='5':
#         reciept = {}
#         while True:
#             name = input('введтите название:')
#             if name == 'n':
#                 break
#             if name in shop:
#                 weight = int(input('введтите вес:'))
#                 if shop[name][2] >= weight:
#                     if name not in reciept:
#                         reciept[name] = weight/100*shop[name][1]
#                     else:
#                         reciept[name] = reciept[name] + weight / 100 * shop[name][1]
#                     shop[name][2] = shop[name][2] - weight
#                     print(shop, reciept)
#                 else:
#                     print('столько товара нет')
#                     break
#             else:
#                 print('товара нет')
#                 break
#         print('ваши покупки:')
#         print(*reciept.keys(), sep=', ')
#         print('цена', sum(reciept.values()))
#         print('осталось :')
#         print(*shop, sep=', ')
#
# В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# баллов и посчитать средний балл по классу
# with open('maks.txt', encoding='utf-8') as file:
#     data = file.read().split('\n')
#     student_marks = {}
#     for row in data:
#         row_list = row.split()
#         name = row_list[0]+' '+row_list[1]
#         student_marks[name] = int(row_list[2])
#     for k, v in student_marks.items():
#         if v < 3:
#             print(k)
#     print('Средний балл', sum(student_marks.values())/len(student_marks))