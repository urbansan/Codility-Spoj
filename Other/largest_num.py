L = [34, 45, 76, 4, 67, 8, 455, 323]
L = [1, 34, 3, 98, 9, 76, 45, 4, 12, 121]
def sortburger(x):
    dl = len(str(x))
    ten_na_dole = 10**(dl-1) or 1
    return float(x) / ten_na_dole


# L.sort(key=lambda x: str(x)[0], reverse=True)
L.sort(key=sortburger, reverse=True)
#
print(L)
# print(sortburger(455))
ZIUTEK = 1
BOLEK = 0
gem1 = [1, 0, 1, 0, 1]
gem2 = [1, 0, 1, 0, 1]
gem3 = [0, 1, 1, 0, 0]
gem4 = [0, 0, 1, 0]
gem5 = [0, 1, 0, 1, ]

gem1 = [ZIUTEK, BOLEK, ZIUTEK, BOLEK, ZIUTEK]
gem2 = [ZIUTEK, BOLEK, ZIUTEK, BOLEK, ZIUTEK]
gem3 = [BOLEK, ZIUTEK, ZIUTEK, BOLEK, BOLEK]
gem4 = [BOLEK, BOLEK, ZIUTEK, BOLEK]
gem5 = [ZIUTEK, ZIUTEK, BOLEK, BOLEK, ZIUTEK]