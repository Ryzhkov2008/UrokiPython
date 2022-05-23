# Задание 4
a = int(input("Введите количество должников: "))
b = 0
sum1 = 0
while b <= a:
    print("должник с номером: ", b)
    summ = int(input("Введите сумму долга: "))
    sum1 += summ
    b+=5
print(sum1)
