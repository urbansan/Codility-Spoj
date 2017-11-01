
def solution(N):
    print(bin(N))
    max_count = 0
    counter = 0
    legit_counter = False
    for el in bin(N).split('b')[1]:

        if el == '1' and legit_counter:
            max_count = max(counter, max_count)
            counter = 0
        elif el == '1':
            legit_counter = True
        elif el == '0' and legit_counter:
            counter += 1
    # max_count = max(counter, max_count)
    return max_count


N = 123
print(solution(N))

N = 1024
print(solution(N))

N = 16
print(solution(N))

N = 51712
print(solution(N))

