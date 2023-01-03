# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
#
# a = int(input())
# print(fib(a-1))


def fibonacci(num):
    if num<=1:
        return num
    return fibonacci(num-1)+fibonacci(num-2)

n=int(input())
print(fibonacci(n))

# for문 구현
# fibonacci = [0, 1]
# for i in range(2, n+1):
#     num = fibonacci[i-1] + fibonacci[i-2]
#     fibonacci.append(num)
