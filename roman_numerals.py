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

    def convert(self, units, multiplyer):
        if units < 1:
            return

        if units in [4, 9]:
            self.append(self.prefix(units, multiplyer))
            return self.append((units + 1) * multiplyer)

        if units % 5 == 0:
            return self.append(units * multiplyer)

        if units > 5:
            self.append(5 * multiplyer)
            return self.convert(units % 5, multiplyer)

        self.append(multiplyer)
        self.convert(units - 1, multiplyer)

    def append(self, index):
        return self.numerals.append(self.LOOKUP[index])

    def prefix(self, units, multiplyer):
        if units * multiplyer <= 10:
            return 1

        keys = list(self.LOOKUP.keys())
        next_index = keys.index((units + 1) * multiplyer)

        if self.is_multiple_of_ten((keys[next_index] / multiplyer)):
            return keys[next_index - 2]

        return keys[next_index - 1]

    def is_multiple_of_ten(self, units):
        return units % 10 == 0
