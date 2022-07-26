import sys


def check_dice(nums):
    num = 0
    cnt = 0
    while len(nums) - 1:
        tmp = nums.pop(0)
        for idx in range(len(nums)):
            if tmp == nums[idx]:
                num = tmp
                cnt += 1
    if cnt == 0:
        num = max(nums)
    return [num, cnt]


def cal_reward(num, cnt):
    if cnt == 3:
        reward = 10000 + num * 1000
        return reward
    elif cnt == 2:
        reward = 1000 + num * 100
        return reward
    else:
        reward = num * 100
        return reward


sys.stdin = open("input.txt", "rt")
n = int(input())
case = list()
for i in range(n):
    num_list = list(map(int, input().split()))
    check = check_dice(num_list)
    case.append(cal_reward(check[0], check[1]))     # check[0] : 중복된 주사위 눈, check[1] : 중복 횟수
print(max(case))



