class LuckyNumbersCounter:

    def count_lucky_numbers_with_formula(self, digit_count: str) -> str:
        """ Returns number of all combinations where sum(first_half_numbers) == sum(second_half_numbers)

        Solution from http://www.ega-math.narod.ru/Quant/Tickets.htm#A2.
        """
        N = int(digit_count)
        result = 0
        for i in range(0, N * 9 + 1):
            n = self._count_N(N, i)
            result += n * n
        return str(result)

    def _count_N(self, digit_number: int, digit: int) -> int:
        if digit_number == 1:
            if 0 <= digit < 10:
                return 1
            else:
                return 0

        sum = 0
        for number in range(10):
            sum += self._count_N(digit_number - 1, digit - number)
        return sum

    def count_lucky_numbers_with_recursion(self, digit_count: str) -> str:
        """ Returns number of all 'lucky' combinations for number with digit_count

        Repeated code from lesson to compare running time for function with formula and with recursion
        """
        self.result = 0
        self._recursion(int(digit_count))
        return str(self.result)

    def _recursion(self, level: int,  previous_index1: int = 0, previous_index2: int = 0):
        if level == 1:
            for index1 in range(10):
                for index2 in range(10):
                    if previous_index1+index1 == previous_index2+index2:
                        self.result += 1
            return
        else:
            for index1 in range(10):
                for index2 in range(10):
                    self._recursion(level-1, previous_index1+index1, previous_index2+index2)
            return

if __name__ == '__main__':
    pass
