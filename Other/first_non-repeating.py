import string
import random
from collections import Counter
chars = [random.choice(string.ascii_uppercase[:10]) for _ in range(20)]

print(*chars, sep='')

def first_non_repeating(chars):
    c = Counter(chars)
    for char in chars:
        if c[char] == 1:
            return char
    return None

def first_non_repeating_harder(chars):
    from collections import defaultdict
    nonrepeating = None
    counter = dict()

    for char in chars:
        if char not in counter:
            counter[char] = 1
        elif:
            




char = first_non_repeating(chars)
char2 = first_non_repeating_harder(chars)
print(char, char2)
