# "Перемножить все черные цифры"
a = 1
b = 1
while a <= 125:
    if a % 2 == 0:
        b *= a
    a+=1
print(b)


