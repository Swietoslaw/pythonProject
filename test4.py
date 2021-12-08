n, k = input().split()
results = list(map(int, input().split()))
boys = 0
k = int(k)-1
j = 0
for i in results:
    if results[j] >= results[k] and results[j] > 0:
        boys += 1
    j += 1
print(boys)