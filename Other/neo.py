import re


instr = '''7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!'''


def drop_nonalpha(matchobj):
    # print(matchobj)
    res = matchobj.group()
    return res[0] + ' ' + res[-1]

def neo(instr):
    lines = [list(line) for line in instr.split('\n')]
    rows = int(lines[0][0])
    cols = int(lines[0][2])
    chars = [lines[row][col]for col in range(cols) for row in range(1, rows+1)]
    txt = ''.join(chars)
    print()
    res = re.sub(r'[a-zA-Z][^a-zA-Z\n]+[a-zA-Z]', drop_nonalpha, txt)

    print(res)

neo(instr)


