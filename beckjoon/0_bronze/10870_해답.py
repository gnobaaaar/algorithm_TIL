# 동적프로그래밍

n = int(input())
#입력만큼 리스트 생성
f = [0] * (n+1)

def pibo(n):
    if(f[n]) != 0:      # f안에 값이 존재한다면
        return f[n]     # 재귀함수를 거치지 않고 그대로 출력
    else{
        if n < 2:
            f[n] = n
            return f[n]
        else:
            f[n] = pibo(n-1) + pibo(n-2)
        return f[n]
    }

print(pibo(n))