
def print_K(K):
    for line in K:
        print(line)
        # print()
    print()

def knapSack(total_weight, item_weights, item_values, items_count):
    highest_values = [[0]*(total_weight+1) for _ in range(items_count)]

    for item_idx in range(-1, items_count):
        for current_weight in range(total_weight+1):
            if current_weight == 0:
                highest_values[item_idx][current_weight] = 0
            elif item_weights[item_idx] <= current_weight:
                highest_values[item_idx][current_weight] = max(
                    item_values[item_idx] + \
                    highest_values[item_idx-1][current_weight - item_weights[item_idx]],
                    highest_values[item_idx-1][current_weight])
            else:
                highest_values[item_idx][current_weight] = \
                    highest_values[item_idx - 1][current_weight]
            print_K(highest_values)
    return highest_values[-1][-1]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))