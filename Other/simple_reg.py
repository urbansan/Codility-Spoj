import re

# line_count = int(input().rstrip())

# lines = [input() for _ in range(line_count)]

# txt = '\n'.join(lines)

txt = '''x&& &&& && && x || | ||\|| x'''
print(txt)
new_txt = re.sub(r'(?<= )\|\|(?= )', 'or', txt)
new_txt = re.sub(r'(?<= )&&(?= )', 'and', new_txt)
# new_txt = re.sub(r' && ', ' and ', new_txt)

print(new_txt)