import math


def prime_list(n):
    sieve = [True] * n
    m = int(math.sqrt(n))  # 약수의 최대값은 n의 제곱근보다 작다.
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n, i):  # 첫 약수를 구한 후 약수의 배수를 모두 False 처리
                sieve[j] = False
    return sieve


num = int(input())
cnt = prime_list(num).count(True) - 2  # 0, 1 포함되어 있기 때문에 -2 해줘여 한다.

print(prime_list(num)[2::])
print(cnt)
