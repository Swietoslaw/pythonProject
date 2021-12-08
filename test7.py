n = list(input())
m = list(input())
a = [x.upper() for x in n]
b = [x.upper() for x in m]
y = []
z = []
for i in a:
    y.append(ord(i))
for j in b:
    z.append(ord(j))

leen = len(y)
za = 0
while leen > 0:
    if y[za] == z[za]:
        leen -= 1
        za += 1
        continue
    elif y[za] > z[za]:
        print(1)
        break
    elif y[za] < z[za]:
        print(-1)
        break

if leen == 0:
    if y[leen - 1] == z[leen - 1]:
        print(0)
