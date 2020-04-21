


def merge_the_tools(string, substr_size):
    n = 0
    while substr_size*n < len(string):
        slice_start = int(n * substr_size)
        slice_end = int((n+1)*substr_size)
        used_letters = set()
        for char in string[slice_start : slice_end]:
            if char not in used_letters:
                print(char, end='')
                used_letters.add(char)
        print()
        n += 1





merge_the_tools('AABCAAADA', 3)

merge_the_tools('DOWTJAHBJKRXASYLDEQQXLQBFHLZXIKAZH', 1)