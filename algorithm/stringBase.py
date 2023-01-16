def solution(s):
    ans = True
    if len(s) == 4 or len(s) == 6:
        for c in s:
            if '0' <= c <= '9':
                if ans == False:
                    continue
            else:
                ans = False
    else:
        ans = False
    return ans


def other_sol(s):
    return s.isdigit() and len(s) in (4, 6)
