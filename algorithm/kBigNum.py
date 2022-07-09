import sys
from itertools import combinations

sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
nums = list(map(int, input().split()))
c_nums = list(combinations(nums, 3))

# 합을 구해서 중복수가 발생하는 것을 생각해야 한다.
sum_nums = set()
for comb in c_nums:
    sum_nums.add(sum(comb))
# for comb in c_nums:
#   sum_nums.append(sum(comb))
# sum_nums.sort(reverse=True)
print(sorted(sum_nums, reverse=True)[k - 1])
