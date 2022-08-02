import sys


def check_ans(n, ans):
    total_score = 0
    cnt = 0
    for val in ans:
        if val == 1:
            # total_score += 1
            cnt += 1
            print(cnt)
        else:
            total_score = total_score + cnt + 1
            cnt = 0

    print(total_score)


sys.stdin = open("input.txt")
n = int(input())
ans = list(map(int, input().split()))
print(ans)
check_ans(n, ans)