import sys

sys.stdin = open("input.txt", "rt")

# 제약 조건
# N과 M은 4, 6, 8, 12, 20 중의 하나

n, m = map(int, input().split())
sum_dict = {}
for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_dict[i + j] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_dict[i + j] += 1

case_cnt = sum_dict.values()
case_val = list(sum_dict.keys())

for idx, val in enumerate(case_cnt):
    if val == max(case_cnt):
        print(case_val[idx], end=" ")
