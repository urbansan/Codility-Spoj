
def solution(S):
    bracket_map = {'(': ')', '[': ']', '{': '}'}
    a = []
    for ch in S:
        if ch in ('(', '{', '['):
            a.append(ch)
        elif not a:
            return 0
        elif ch == bracket_map[a[-1]]:
            a.pop(-1)
        else:
            return 0
    if a:
        return 0
    return 1

def solution(S):
    a = []
    for ch in S:
        if ch in ('(', '{', '['):
            a.append(ch)
        elif not a:
            return 0
        elif ch == ')' and a[-1] == '(':
            a.pop(-1)
        elif ch == '}' and a[-1] == '{':
            a.pop(-1)
        elif ch == ']' and a[-1] == '[':
            a.pop(-1)
        else:
            return 0
    if a:
        return 0
    return 1

from datetime import datetime as dt

if __name__ == '__main__':
    start = dt.now()
    S = '{[()()]}'
    print(solution(S))
    S = "([)()]"
    print(solution(S))
    S = ""
    print(solution(S))
    S = "}}))]]"
    print(solution(S))
    S = "({[{[{[{{(())}}]}]}]})"
    print(solution(S))
    S = "((("
    print(solution(S))
    S = "("*100000 + ")"*100000
    print(solution(S))

    # S = "("*100000 + ")"*100000
    # print(solution(S))

    print(str(dt.now()-start))
