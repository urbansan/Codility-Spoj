from collections import Counter

vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}


def vowel_consonant_counter(txt):
    vowel_points = 0
    consonant_points = 0
    for char, count in Counter(txt):
        if char in vowels:
            vowel_points += count
        else:
            consonant_points += count

    return vowel_points, consonant_points

def minion_game(instr):
    # vowel_points, consonant_points = vowel_consonant_counter(instr)
    word = list(map(lambda x: x in vowels, instr))

    kevin = 0
    kevin_word_count = 0
    stuart = 0
    stuart_word_count = 0
    for is_vowel, char in zip(word, instr):

        if is_vowel:
            kevin += 1
        else:
            stuart += 1

        if kevin > 0:
            kevin_word_count += kevin
        if stuart > 0:
            stuart_word_count += stuart

        # print(is_vowel, char)
    if kevin_word_count ==  stuart_word_count:
        print('Draw')
    elif kevin_word_count > stuart_word_count:
        print('Kevin', kevin_word_count)
    else:
        print('Stuart', stuart_word_count)
    # print(f'kevin = {kevin_word_count}, stuart = {stuart_word_count}')

    # b a n a n a






minion_game('banana')
minion_game('Banana')



