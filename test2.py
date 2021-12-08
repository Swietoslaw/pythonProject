y = []
x = int(input())
w = x

while w > 0:
    w = w - 1
    y.append(input())
for i in y:
    if len(i) > 10:
        print(i[0], (len(i) - 2), i[len(i)-1], sep="")
    else:
        print(i)
