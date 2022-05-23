##  "калькулятор, деление на 0 "
a = float(input( "введите число 1:  "))
b = float(input ("введите число 2:  "))
d = input("введите действие")
while True:
    if d == "+":
        print(a+b)
        break
    elif d == "-":
        print(a-b)
    elif d == "*":
         print(a*b)
    elif d == "/":
        if d == 0:
            print("делить на 0 нельзя")





