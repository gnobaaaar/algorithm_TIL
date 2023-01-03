len = int(input())
a = list(map(int, input().split()))
max = max(a)
total = 0

for i in range(len):
    total += (a[i]/max) * 100

print(total/len)

# sum(a)가 더 적은 소요시간을 가진다