def solution(N, A):
    global_max = 0
    current_max = 0
    counter = [0] * N
    for el in A:
        n = el - 1
        if el > N:
            global_max = current_max
        else:
            if counter[n] < global_max:
                counter[n] = global_max
            counter[n] += 1
            current_max = max(current_max, counter[n])

    return [global_max if el < global_max else el for el in counter]