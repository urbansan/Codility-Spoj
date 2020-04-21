from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    word_counter = Counter(magazine)
    for word in note:
        word_type_left = word_counter.get(word, 0)
        if word_type_left == 0:
            print('No')
            break
        else:
            word_counter[word] -= 1
    else:
        print('Yes')





t0_mag = ['give', 'me', 'one', 'grand', 'today', 'night']
t0_note = ['give', 'one', 'grand', 'today']

t1_mag = ['two', 'times', 'three', 'is', 'not', 'four']
t1_note = ['two', 'times', 'two', 'is', 'four']


t2_mag = ['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts']
t2_note = ['ive', 'got', 'some', 'coconuts']

checkMagazine(t0_mag, t0_note)
checkMagazine(t1_mag, t1_note)
checkMagazine(t2_mag, t2_note)