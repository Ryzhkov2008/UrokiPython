#
a = [1, 5, 2, 4, 5, 7, 8 ]
b = 0
d = 0
for i in a:
    if i % 2 == 0:
        b+=1
    else:
        d+=1
if b>d:
        s = sum(a)
        print("сумма =", s)
else:
    print("произведение =", a[1]*a[3]*a[6])






