from collections import OrderedDict


class Numeral:

    NUMERALS = OrderedDict({
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
        if not isinstance(n, int) or isinstance(n, bool):
            return

        for index, i in enumerate(str(n)):
            self._convert(int(i), self.MULTIPLYERS[len(str(n)) - index])

        return ''.join(self.numerals)

    def _convert(self, units, multiplyer):
        if units < 1:
            return

        if self._is_double_numeral(units):
            self._append(self._prefix(units, multiplyer))
            return self._append((units + 1) * multiplyer)

        if units % 5 == 0:
            return self._append(units * multiplyer)

        if units > 5:
            self._append(5 * multiplyer)
            return self._convert(units % 5, multiplyer)

        self._append(multiplyer)
        self._convert(units - 1, multiplyer)

    def _is_double_numeral(self, units):
        return units in [4, 9]

    def _append(self, index):
        return self.numerals.append(self.NUMERALS[index])

    def _prefix(self, units, multiplyer):
        if units * multiplyer <= 10:
            return 1

        keys = list(self.NUMERALS.keys())
        next_index = keys.index((units + 1) * multiplyer)

        if self._is_multiple_of_ten((keys[next_index] / multiplyer)):
            return keys[next_index - 2]

        return keys[next_index - 1]

    def _is_multiple_of_ten(self, units):
        return units % 10 == 0
