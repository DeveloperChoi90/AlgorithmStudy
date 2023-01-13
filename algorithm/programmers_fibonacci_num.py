def solution(n : int):
    if n < 2:
        return n
    else:
        return (solution(n - 2) + solution(n - 1)) % 1234567


def fibo(n : int):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a % 1234567


n = 100000
print(solution(n))
