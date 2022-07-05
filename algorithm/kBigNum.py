import sys
from itertools import combinations

sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
nums = list(map(int, input().split()))
c_nums = list(combinations(nums, 3))
# print(c_nums)
sum_nums = list()
for comb in c_nums:
    sum_nums.append(sum(comb))

sum_nums.sort(reverse=True)
print(sum_nums[k - 1])
