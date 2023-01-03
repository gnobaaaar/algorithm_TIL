def solution(x, n):
    answer = []
    key = x
    for i in range(n):
        answer.append(x)
        x = x + key

    return answer