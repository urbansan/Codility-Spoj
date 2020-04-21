import math
from collections import defaultdict
from itertools import product
from itertools import combinations_with_replacement as cwr
from itertools import combinations

from collections import Counter


def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0

    for v in arr:
        if v in r3:
            count += r3[v]
        if v in r2:
            r3[v * r] += r2[v]
        r2[v * r] += 1
        print(count, v, r2, r3)
    print(count)
    return count


    # print(power_to_positions)



# countTriplets([1, 2, 2, 4], 2)
# countTriplets([1, 3, 9, 9, 27, 81], 3)
# countTriplets([1, 5, 5, 25, 125], 5)
# countTriplets([5, 25, 125, 25, 125, 5], 5)
countTriplets([5, 25, 125, 25, 625, 125, 5, 125, 625], 5)

# countTriplets([1] * 100, 1)
