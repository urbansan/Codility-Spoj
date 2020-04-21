

def word_order(strings):
    used_strings = dict()
    for string_ in strings:
        if string_ not in used_strings:
            used_strings[string_] = 1
        else:
            used_strings[string_] += 1
    print(len(used_strings))
    print(*used_strings.values())

A = [
    'bcdef',
    'abcdefg',
    'bcde',
    'bcdef',
]

word_order(A)


