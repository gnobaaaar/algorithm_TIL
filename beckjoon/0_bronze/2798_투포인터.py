def solution(n, target)-> int:
    a = list(map(int, input().split()))
    a.sort()

    result = 0
    for i in range(n-2):
        left = i+1
        right = len(a)-1

        while left < right:
            sum = a[i] + a[left] + a[right]

            if sum == target:
                return sum
            elif sum > target:
                right -= 1
            else:
                if sum > result:
                    result = sum
                left +=1
    return result



n, target = map(int, input().split())
print(solution(n, target))