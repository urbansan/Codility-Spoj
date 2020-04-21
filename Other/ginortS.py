import string


class ginsortS1324:
    def __init__(self):
        self.value_map = self._build_value_map()

    def _build_value_map(self):
        value_map = dict()
        value = 0
        for char in string.ascii_lowercase:
            value_map[char] = value
            value += 1

        for char in string.ascii_uppercase:
            value_map[char] = value
            value += 1

        for digit in range(1, 10, 2):
            value_map[str(digit)] = value
            value += 1

        for digit in range(0, 10, 2):
            value_map[str(digit)] = value
            value += 1
        print(value_map)
        return value_map

    def _sort_func(self, value):
        return self.value_map.get(value, 200)

    def sort(self, string_):
        str_list = list(string_)
        print(str_list)
        str_list.sort(key=self._sort_func)
        print(''.join(str_list))

sorter = ginsortS1324()
sorter.sort('Sorting1234')

