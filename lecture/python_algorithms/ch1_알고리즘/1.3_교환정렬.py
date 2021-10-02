def exchange(S):
    n = len(S)
    for i in range(n-1):
        for j in range(i+1, n):
            if S[i] > S[j]:
                S[i], S[j] = S[j], S[i] # swap
