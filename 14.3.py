# Пользователь - продавец магазина. Вам нужно написать программу,
# которая будет спрашивать у пользователя, какие товары имеются в
# магазине то тех пор, пока пользователь не вводит пустую строчку.
# Каждый товар пишется в отдельную строку в файле shop.txt.
# Итоговый файл выглядит следующим образом:
import os

with open("shop.txt", mode="a", encoding="utf-8") as file:
    shop_txt = []
    while True:
        a = input("Введите товар: ")
        if a == "":
            break
        file.write(a + "\n")
        shop_txt.append(a)

with open("resiept.txt", mode="a", encoding="utf-8") as file:
    while True:
        produkt = input("Выберите товар: ")
        if produkt == "":
            print("Спасибо за покупку!")
            break
        elif produkt in shop_txt:
            file.write(produkt + "\n")
        else:
            print("Такого продукта нет")

