# 입력설명
# 첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상 N 이하이다.
# 출력설명
# 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 -1을 출력하시오.
k, n = map(int, input().split())
k_div = [k % val for val in range(1, k + 1)]  # 입력된 N의 약수를 구하기 위해 : 나머지가 0인 경우가 N의 약수이다.
k_divisor = list()
for idx, val in enumerate(k_div):
    if val == 0:
        k_divisor.append(idx + 1)

print(k_divisor[n - 1])
