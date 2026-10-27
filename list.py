a = [x for x in range(1,151)]
b =[]
for i in a:
    if i%5==0 or i%7==0:
        b.append(i)

print(b)