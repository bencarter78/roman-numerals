from collections import OrderedDict


class Numeral:

    LOOKUP = OrderedDict({
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    })

    MULTIPLYERS = {
        1: 1,
        2: 10,
        3: 100,
        4: 1000
    }

    def __init__(self):
        self.numerals = []

    def generate(self, n):
        for index, i in enumerate(str(n)):
            self.convert(int(i), self.MULTIPLYERS[len(str(n)) - index])

        return ''.join(self.numerals)

    def convert(self, n, multiplyer):
        if n < 1:
            return

        if self.is_prefixable(n):
            self.append(self.prefix(n, multiplyer))
            return self.append((n + 1) * multiplyer)

        if n % 5 == 0:
            return self.append(n * multiplyer)

        if n > 5:
            self.append(5 * multiplyer)
            return self.convert(n % 5, multiplyer)

        self.append(multiplyer)
        self.convert(n - 1, multiplyer)

    def is_prefixable(self, n):
        return n in [4, 9]

    def prefix(self, n, multiplyer):
        if n * multiplyer <= 10:
            return 1

        keys = list(self.LOOKUP.keys())
        next_index = keys.index((n + 1) * multiplyer)

        if self.is_multiple_of_ten((keys[next_index] / multiplyer)):
            return keys[next_index - 2]

        return keys[next_index - 1]

    def is_multiple_of_ten(self, n):
        return n % 10 == 0

    def append(self, index):
        return self.numerals.append(self.LOOKUP[index])
