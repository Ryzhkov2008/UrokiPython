#
import random

a = random.randint(1, 10)
b = random.randint(1, 2)
if b == 2:
    b = "красное"
else:
    b = "черное"
s = 1
while s <= 5:
    print("попытка N", s)
    p = int(input("введите число от 1 до 10:  "))
    p1 = input("введите число от 1 до 2:  ")
    if p == a and p1 == b:
        print("Победа !!!")
        break
    elif p != a:
        print("Попробуйте еше раз")
    s +=1
else:
    print("Вы не угадали, выигрышная комбинация ", a, b)



