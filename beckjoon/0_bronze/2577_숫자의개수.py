a = int(input())
b = int(input())
c = int(input())
total_list = list(map(int, str(a*b*c)))

def lower_bound(list, target):
    start, end = 0, len(list)
    while start < end:
        mid = (start+end) //2
        if list[mid] < target:
            start = mid +1
        else:
            end = mid
    return end

def upper_bound(list, target):
    start, end = 0, len(list)
    while start < end:
        mid = (start+end) //2
        if list[mid] <= target:
            start = mid +1
        else:
            end = mid
    return end

total_list.sort()
# print(total_list)
for i in range(10):
    print(upper_bound(total_list,i) - lower_bound(total_list,i))