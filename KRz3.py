# Задание 3
import random

a = random.randint(1, 10)

s = 1
print("Введите число от 1 до 10 : ")
while s <= 10:
    p = int(input())
    if p == a:
        print("Вы угадали! Число попыток: ", s)
        break
    elif p > a:
        print("Число больше. Попробуйте еше раз")
    elif p < a:
        print("Число меньше. Попробуйте еше раз")
    s +=1

