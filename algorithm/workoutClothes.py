def solution(n, lost, reserve):
    participants = n
    cnt = 0
    new_lost = [i for i in lost if i not in reserve]
    new_lost.sort()
    new_reserve = [i for i in reserve if i not in lost]
    new_reserve.sort()
    for lost_student in new_lost:
        if len(new_reserve) == 0:
            break
        elif (lost_student - 1) in new_reserve:
            new_reserve.remove((lost_student - 1))
            cnt += 1
        elif (lost_student + 1) in new_reserve:
            new_reserve.remove((lost_student + 1))
            cnt += 1
    return participants - len(lost) + cnt + (len(lost) - len(new_lost))


def other_sol(n, lost, reserve):
    new_reserve = [r for r in reserve if r not in lost]
    new_lost = [l for l in lost if l not in reserve]
    for r in new_reserve:
        f = r - 1
        b = r + 1
        if f in new_lost:
            new_lost.remove(f)
        elif b in new_lost:
            new_lost.remove(b)
    return n - len(new_lost)


n = 5
lost = [2, 4]
reserve = [1, 3]
print(other_sol(n, lost, reserve))
