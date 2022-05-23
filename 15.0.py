
t = [-1, 2, 9, -1, -2]
change_count = 0
for i in range(ltn(t)-1):
    if t[i]>0 and t[i+1]<0 or t[i]> 0 and t[i+1] >0:
        change_count += 1
print(change_count)
