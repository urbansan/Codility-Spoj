

def max_subset_sum_recursive(arr, current_idx=0, current_sum=None):
    try:
        el_value = arr[current_idx]
    except IndexError:
        return current_sum

    new_sum = current_sum + el_value if current_sum is not None else el_value
    current_el_taken = max_subset_sum_recursive(arr, current_idx + 2, new_sum)
    current_el_not_taken = max_subset_sum_recursive(arr, current_idx + 1, current_sum)
    if current_el_not_taken is None:
        return current_el_taken
    else:
        return max(current_el_taken, current_el_not_taken)

def max_subset_sum(arr):

    prev_3_steps = arr[0]
    prev_2_steps = arr[1]
    prev_step = max(prev_2_steps, prev_3_steps + arr[2], arr[2], prev_3_steps)

    for elx in arr[3:]:
        current_max = max(prev_2_steps + elx, prev_2_steps, prev_3_steps + elx, elx, prev_3_steps)
        prev_step, prev_2_steps, prev_3_steps = current_max, prev_step, prev_2_steps
    return max(prev_step, prev_2_steps)





t0 = [-2, 1, 3, -4, 5]  # 8
t1 = [3, 7, 4, 6, 5]  # 13
t2 = [3, 5, -7, 8, 10] # 15

# result = max_subset_sum(t0)
# result = max_subset_sum(t1)
# result = max_subset_sum(t2)
# result = max_subset_sum_recursive(t2)
# print(result)



# t2 = [3, 5, -7, 8, 10] # 15

with open('test_cases/max_array_subset_01.txt', 'r') as f:
    f.readline()  # skip line
    arr = list(map(int, f.readline().split()))
result = max_subset_sum(arr)
print(result)

#
# val = 81656345 - 81660407
# print(val)