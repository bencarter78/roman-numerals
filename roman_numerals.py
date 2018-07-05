class Numeral:

    LOOKUP = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    def __init__(self):
        self.number_as_string = ''
        self.numeral = []

    def generate(self, n):
        """
        Generate the corresponding Roman Numeral for a given integer
        """
        self.number_as_string = str(n)

        if len(self.number_as_string) == 4:
            self.thousands(int(self.number_as_string[0]))
            self.number_as_string = self.number_as_string[1:]

        if len(self.number_as_string) == 3:
            self.hundreds(int(self.number_as_string[0]))
            self.number_as_string = self.number_as_string[1:]

        if len(self.number_as_string) == 2:
            self.tens(int(self.number_as_string[0]))
            self.number_as_string = self.number_as_string[1:]

        self.ones(int(self.number_as_string[0]))

        return ''.join(self.numeral)

    def ones(self, n):
        """
        Determine the numerals for the ones column
        """
        multiplyer = 1

        if n < 1:
            return

        if n in [4, 9]:
            self.numeral.append(self.LOOKUP[1])
            return self.numeral.extend(self.LOOKUP[n + multiplyer])

        if n % 5 == 0:
            return self.numeral.append(self.LOOKUP[n])

        if n > 5:
            self.numeral.append(self.LOOKUP[5])
            return self.ones(n % 5)

        self.numeral.append(self.LOOKUP[multiplyer])

        self.ones(n - 1)

    def tens(self, n):
        """
        Determine the numerals for the tens column
        """
        multiplyer = 10

        if n < 1:
            return

        if n in [4, 9]:
            self.numeral.append(self.LOOKUP[multiplyer])
            return self.numeral.extend(self.LOOKUP[(n + 1) * multiplyer])

        if n % 5 == 0:
            return self.numeral.append(self.LOOKUP[n * multiplyer])

        if n > 5:
            self.numeral.append(self.LOOKUP[50])
            return self.tens(n % 5)

        self.numeral.append(self.LOOKUP[multiplyer])

        self.tens(n - 1)

    def hundreds(self, n):
        """
        Determine the numerals for the hundreds column
        """
        multiplyer = 100

        if n < 1:
            return

        if n in [4, 9]:
            self.numeral.append(self.LOOKUP[multiplyer])
            return self.numeral.extend(self.LOOKUP[(n + 1) * multiplyer])

        if n % 5 == 0:
            return self.numeral.append(self.LOOKUP[n * multiplyer])

        if n > 5:
            self.numeral.append(self.LOOKUP[500])
            return self.hundreds(n % 5)

        self.numeral.append(self.LOOKUP[multiplyer])

        self.hundreds(n - 1)

    def thousands(self, n):
        """
        Determine the numerals for the thousands column
        """
        multiplyer = 1000

        if n < 1:
            return

        if n in [4, 9]:
            self.numeral.append(self.LOOKUP[multiplyer])
            return self.numeral.extend(self.LOOKUP[(n + 1) * multiplyer])

        if n % 5 == 0:
            return self.numeral.append(self.LOOKUP[n * multiplyer])

        if n > 5:
            self.numeral.append(self.LOOKUP[500])
            return self.thousands(n % 5)

        self.numeral.append(self.LOOKUP[multiplyer])

        self.thousands(n - 1)
