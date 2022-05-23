# Задание 1
sp = [4, 3, 5, 2, 5, 1, 3, 5, 6]

count = []
filtered = []

for a in sp:
    if a in count:
        filtered.append(a)
        count.remove(a)
    if a not in filtered:
        count.append(a)

print(count)


