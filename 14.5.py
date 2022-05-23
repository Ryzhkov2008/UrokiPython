#
# n = int(input("Введите число: "))
# for i in range(n):
#   b = i**2
#   print(b)


n = input("Введите число - ")
num = int(n)
summa = 0
for i in range(len(n)):
    summa += (num % 10**(i+1)) // 10**i
print(summa)
