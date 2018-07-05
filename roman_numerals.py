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
        self.number_as_string = ''
        self.numeral = []

    def generate(self, n):
        """
        Generate the corresponding Roman Numeral for a given integer
        """
        self.number_as_string = str(n)

        while len(self.number_as_string) > 0:
            self.calculate(
                int(self.number_as_string[0]), self.MULTIPLYERS[len(self.number_as_string)])
            self.remove_leading_column()

        return ''.join(self.numeral)

    def calculate(self, n, multiplyer):
        """
        Determine the numerals for the given column
        """
        if n < 1:
            return

        if n in [4, 9]:
            if n * multiplyer <= 10:
                pre_numeral = self.LOOKUP[1]
            else:
                keys = list(self.LOOKUP.keys())
                next_index = keys.index((n + 1) * multiplyer)
                if (keys[next_index] / multiplyer) % 10 == 0:
                    pre_numeral = self.LOOKUP[keys[next_index - 2]]
                else:
                    pre_numeral = self.LOOKUP[keys[next_index - 1]]

            self.numeral.append(pre_numeral)
            return self.numeral.extend(self.LOOKUP[(n + 1) * multiplyer])

        if n % 5 == 0:
            return self.numeral.append(self.LOOKUP[n * multiplyer])

        if n > 5:
            self.numeral.append(self.LOOKUP[5 * multiplyer])
            return self.calculate(n % 5, multiplyer)

        self.numeral.append(self.LOOKUP[multiplyer])

        self.calculate(n - 1, multiplyer)

    def remove_leading_column(self):
        self.number_as_string = self.number_as_string[1:]
