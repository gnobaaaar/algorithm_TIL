n, target = map(int, input().split())
a = list(map(int, input().split()))
result = []

for i in range(n):
    for j in range(i+1, n):
        for z in range(j+1, n):
            if a[i] + a[j] + a[z] <= target:
                result.append(a[i] + a[j] + a[z])

print(max(result))