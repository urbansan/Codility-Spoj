def solution(H):
    stack = []
    num_blocks = 0
    for lvl in H:
        # print(lvl, stack, num_blocks)
        if not stack or lvl > stack[-1]:
            stack.append(lvl)
            num_blocks += 1
        elif lvl == stack[-1]:
            pass
        elif stack:
            while stack and lvl < stack[-1]:
                stack.pop(-1)
            if not stack or lvl > stack[-1]:
                stack.append(lvl)
                num_blocks += 1
        # print(lvl, '[' + str(num_blocks) + ']', end=', ')
    return num_blocks


H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
print(solution(H))
H = [1, 1, 1, 1, 1, 1, 1]
print(solution(H))
H = [1, 1, 1, 1, 3, 3, 3, 1, 1, 1]
print(solution(H))
H = []
print(solution(H))
H = [8, 8, 5, 7, 9, 8, 7, 4, 8] * 100000
print(solution(H))
H = [8, 8, 5, 7, 9, 8, 7, 4, 8] * 2

print(solution(H))

