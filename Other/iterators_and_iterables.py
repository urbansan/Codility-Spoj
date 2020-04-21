from itertools import combinations


def probability_of_a_in_combinations(str_list, group_size):
    all_combinations = 0
    count_of_a = 0
    for combination in combinations(str_list, group_size):
        # print(combination)
        all_combinations += 1
        if 'a' in combination:
            count_of_a +=1

    print(round(count_of_a / all_combinations, 4))

probability_of_a_in_combinations(['a', 'a', 'c', 'd'], 1)
