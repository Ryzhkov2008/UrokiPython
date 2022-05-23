# Работа с файлами
# file = open("text.txt", mode="r", encoding="utf-8")
# text = file.read()
# print(text)
# file.close()

# with open("text.txt", mode="r", encoding="utf-8") as file:
#     text = file.read()
#     print(text)

# with open("text.txt", mode="r", encoding="utf-8") as file:
#     text = file.read().split("\n")
#     print(text, type(text))

# with open("text.txt", mode="a", encoding="utf-8") as file:
#      text = file.writelines(["хорошего дня\n", "bye\n"])
#      print(text, type(text))

# Пользователь - продавец магазина. Вам нужно написать программу,
# которая будет спрашивать у пользователя, какие товары имеются в
# магазине то тех пор, пока пользователь не вводит пустую строчку.
# Каждый товар пишется в отдельную строку в файле shop.txt.
# Итоговый файл выглядит следующим образом:
with open("shop.txt", mode="a", encoding="utf-8") as file:
    while True:
        a = input("Введите товар: ")
        if a == "":
            break
        file.write(a+"\n")