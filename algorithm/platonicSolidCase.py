import sys


# 제약 조건
# N과 M은 4, 6, 8, 12, 20 중의 하나
def my_sol(a, b):
    sum_dict = {}
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            sum_dict[i + j] = 0

    for i in range(1, a + 1):
        for j in range(1, b + 1):
            sum_dict[i + j] += 1

    case_cnt = sum_dict.values()
    case_val = list(sum_dict.keys())

    for idx, val in enumerate(case_cnt):
        if val == max(case_cnt):
            print(case_val[idx], end=" ")


def other_sol(a, b):
    sum_list = [0] * (a + b + 1)

    for i in range(1, a + 1):
        for j in range(1, b + 1):
            sum_list[i + j] += 1

    for idx, val in enumerate(sum_list):
        if val == max(sum_list):
            print(idx, end=" ")


sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
my_sol(n, m)
print()
other_sol(n, m)
