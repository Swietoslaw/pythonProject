y = []
x = int(input())
w = x
b = 0

while w > 0:
    w = w - 1
    y.append(input())
for i in y:
    a = int(i[0]) + int(i[2]) + int(i[4])
    if a > 1:
        b += 1
print(b)
