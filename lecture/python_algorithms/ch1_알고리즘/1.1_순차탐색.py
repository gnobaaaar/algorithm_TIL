# n은 개수 S는 리스트, x는 목표값
def seqsearch(n, S, x):
    location = 1
    while location <= n and S[location] != x:
        location += 1
    if location > n:
        location = 0 # 존재하지 않으면 0을 리턴
    return location

S = [0, 1, 2, 3, 4, 5, 6]
x = 5
location = seqsearch(len(S)-1, S, x)
print('location =', location)