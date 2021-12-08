y = []
x = int(input())
w = x
a = 0
while w > 0:
    w = w - 1
    y.append(input())
for i in y:
    if i == "X++" or i == "++X":
        a+=1
    if i == "X--" or i == "--X":
        a-=1

print(int(a))