# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시 #
# 입력 #
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
import sys

sys.stdin = open("input.txt", "rt")
n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

# Bubble Sort
for i in range(len(num_list)):
    for j in range(len(num_list)):
        if num_list[i] < num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

#     num_list.append(tmp)
# num_list.sort(reverse=True)
for num in num_list:
    print(num)


# 처음 답
# n = int(input())
# num_list = []
# for i in range(n):
#     tmp = int(input())
#     num_list.append(tmp)
# num_list.sort()
# for num in num_list:
#     print(num)