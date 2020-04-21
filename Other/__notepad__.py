import re

re_cp = re.compile(r'[a-zA-Z\d_-]+@[a-zA-Z\d]+\.[a-zA-Z]{1,3}', flags=re.ASCII)

A = [
    'dheeraj-234@gmail.com',
    'itsallcrap',
    'harsh_1234@rediff.in',
    'kunal_shin@iop.az',
    'matt23@@india.in',
    'learn.point@learningpoint.net',
    'learnpoint@learningpoint.net',
    'learnpoint@learningpoint.net1']


def fun(s):
    return re_cp.match(s)


for str_ in A:
    print(re_cp.match(str_), str_)


a = a + 10**idx if idx != 0 else 1; print(a*i)