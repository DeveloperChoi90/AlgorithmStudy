import sys
import time

sys.stdin = open("input.txt", "rt")

student_cnt = int(input())
student_scores = list(map(int, input().split()))
scores_mean = round(sum(student_scores) / student_cnt)
start_time = time.time()
# 학생 점수에서 평균을 빼서 제곱한 값이 가장 작은게 대표값이 된다.
representative_nums = [pow((score - scores_mean), 2) for score in student_scores]
end_time = time.time()

# 제곱근이 같을 때 처리를 어떻게 할까?
# print(representative_nums)
for idx, val in enumerate(representative_nums):
    if min(representative_nums) == val:
        if scores_mean < student_scores[idx]:
            print(scores_mean, idx + 1)
            break
        elif scores_mean == student_scores[idx]:
            print(scores_mean, idx + 1)
            break
