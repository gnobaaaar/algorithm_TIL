def return_cnt(num, target):
    cnt = 0
    tmp = num
    while tmp >= 0:
        tmp = tmp - target
        cnt += 1
    return cnt

n = int(input())
a_list = list(map(int, input().split()))
y = 0
m = 0

for i in a_list:
    y += return_cnt(i, 30) * 10
    m += return_cnt(i, 60) * 15

if y < m:
    print('Y {}'.format(y))
elif y > m:
    print('M {}'.format(m))
else:
    print('Y M {}'.format(y))