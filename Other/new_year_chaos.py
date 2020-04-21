def how_many_larger_than(label, slice):
    return sum([label < el for el in slice])

def how_many_smaller_than(label, slice):
    counter = 0
    for el in slice:
        if label > el:
            counter += 1
    return counter


def minimumBribes(q):
    cumulative = 0
    for position, label in enumerate(q, start=1):
        bribe_count = label - position
        if bribe_count > 2:
            print('Too chaotic')
            break
        # print(label, q[label-2: position], label-2, position)
        # larger_count = sum(el > label for el in q[max(label-2, 0): position])
        larger_count = how_many_smaller_than(label, q[position:])
        cumulative += larger_count

    else:
        print(cumulative)


    #

orig = [1, 2, 3, 4, 5, 6, 7, 8]
t0 = [2, 1, 5, 3, 4]
t1 = [1, 2, 5, 3, 7, 8, 6, 4]
t2 = [1, 2, 5, 3, 4, 7, 8, 6]

minimumBribes(t2)

# cumulative = []
# prev = 0
# for position, label in enumerate(t1, start=1):
#     cos = label - position
#     prev += cos if cos > 0 else 0
#     print(prev, end=', ')
#
#
# print(cumulative)
