import sys

# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요.
# 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.


def digit_sum(x):
    if x < 10:
        return x
    else:
        return (x % 10) + digit_sum(x // 10)


sys.stdin = open("input.txt", "rt")

n = int(input())
nums = list(map(int, input().split()))

max_num = 0
ans = 0
for num in nums:
    sum_num = digit_sum(num)
    if sum_num > max_num:
        max_num = sum_num
        ans = num

print(ans)


