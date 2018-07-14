def solution(X, A):
    if len(A) < X:
        return -1

    leaves_positions = [False] * X
    steps_left = X
    for i, el in enumerate(A):
        if not leaves_positions[el - 1]:
            leaves_positions[el - 1] = True
            steps_left -= 1
            if not steps_left:
                return i
    return -1
