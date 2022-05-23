# Задание
count_positiv = 0
count_negativ =0
rait = 1
while True:
    rait = int(input("Введите оценку: "))
    if rait > 0:
        count_positiv +=1
    if rait < 0:
        count_negativ += 1
    elif rait == 0:
        break
print("Количестрово положительных",count_positiv)
print("Количестрово отрицательных",count_negativ)
