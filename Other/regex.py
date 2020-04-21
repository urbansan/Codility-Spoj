import re


str_ = 'axabax'
str_ = '552524'
# str_ = '552524123'


# pat = r'(?=\d*5\d5)(?=\d*2\d2)[0-9]{6}'
pat =r"^(?=\d*(0)\d0)?(?=\d*(1)\d1)?(?=\d*(2)\d2)?(?=\d*(3)\d3)?(?=\d*(4)\d4)?(?=\d*(5)\d5)?(?=\d*(6)\d6)?(?=\d*(7)\d7)?(?=\d*(8)\d8)?(?=\d*(9)\d9)?[0-9]{6}$"
res = re.findall(pat, str_)
print(res)

print(res, len(res))
# print(res)
# if res:
#     print(res.groups(), sep="\n")
P = str_
regex_integer_in_range = ''
regex_alternating_repetitive_digit_pair = r"^(?=\d*(0)\d0)?(?=\d*(1)\d1)?(?=\d*(2)\d2)?(?=\d*(3)\d3)?(?=\d*(4)\d4)?(?=\d*(5)\d5)?(?=\d*(6)\d6)?(?=\d*(7)\d7)?(?=\d*(8)\d8)?(?=\d*(9)\d9)?[0-9]{6}$"
regex_alternating_repetitive_digit_pair = ''
val = (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
print(val)

print(re.findall(r'(?=(\d)\d\1)', '110000'))