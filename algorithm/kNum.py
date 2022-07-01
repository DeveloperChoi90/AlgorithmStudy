# 문제
# N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서
# s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.

# 입력설명
# 첫 번째 줄에 테스트 케이스 T(1<=T<=10)이 주어집니다.
# 각 케이스별
# 첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다. 두 번째 줄에 N개의 숫자가 차례로 주어진다.

# 출력설명
# 각 케이스별 k번째 수를 아래 출력예제와 같이 출력하세요.
import sys

sys.stdin = open("input.txt", "rt")

case = int(input())
for idx in range(case):
    n, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))
    sel_num = sorted(nums[s - 1: e])
    print("#%d %d" % (idx + 1, sel_num[k - 1]))
