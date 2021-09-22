string = input()

repalce = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in repalce:
    # 외우자 새꺄
    string = string.replace(i, '*')

print(len(string))