num = int(input())

for i in range(1, num):
    print('*'*i+' '*(num-i)+' '*(num-i)+'*'*i)
print('*'*2*num)
for i in range(num-1, 0, -1):
    print('*'*i+' '*(num-i)+' '*(num-i)+'*'*i)