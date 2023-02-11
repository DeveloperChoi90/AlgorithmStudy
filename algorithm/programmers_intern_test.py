def solution(lotteries):
    win_percent = []
    win_amount = []
    for lottery in lotteries:
        win_percent.append(lottery[0] / (lottery[1] + 1))
        win_amount.append(lottery[2])
    if len(set(win_percent)) == len(win_percent):
        return win_percent.index(max(win_percent)) + 1
    else:
        if max(win_percent) < 1:
            if win_amount[win_percent.index(max(win_percent))] > win_amount[win_amount.index(max(win_amount))]:
                return win_percent.index(max(win_percent)) + 1
            else:
                return win_amount.index(max(win_amount)) + 1
        else:
            tmp_percent = []
            for x in win_percent:
                if x > 1:
                    tmp_percent.append(win_percent.index(x))
            tmp_amount = [win_amount[val] for val in tmp_percent]
            return tmp_percent[tmp_amount.index(max(tmp_amount))]


lotteries = [[50, 1, 50], [50, 0, 100], [50, 1, 500], [50, 1, 1000]]
print(solution(lotteries))


def solution2(grid):
    answer = 0
    trans_grid = []
    col = 0
    row = len(grid)
    for rows in grid:
        col += 1
        for x in rows:
            if x == ".":
                trans_grid.append(0)
            else:
                trans_grid.append(1)
    return answer


# SELECT BRANCH_ID, NAME FROM EMPLOYEES
# WHERE SALARY = (SELECT MAX(SALARY) FROM EMPLOYEES)
# ORDER BY BRANCH_ID, NAME

# select BRANCH_ID, NAME
# from Employees
# where (BRANCH_ID, SALARY) in
# (select BRANCH_ID, max(SALARY)
# from Employees
#     group by BRANCH_ID
# )
# order by BRANCH_ID, NAME