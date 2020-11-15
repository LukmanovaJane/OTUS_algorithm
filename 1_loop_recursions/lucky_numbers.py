def count_lucky_numbers(digit_count: str) -> str:
    """ Counts all combinations where sum(first_half_numbers) == sum(second_half_numbers)

    Solution from www.ega-math.narod.ru/Quant/Tickets.htm#A2
    """
    N = int(digit_count)
    tickets = 0
    for i in range(0, N*9+1):
        n = count_N(N, i)
        tickets += n*n
    return str(tickets)


def count_N(digit_number: int, digit: int) -> int:
    if digit_number == 1:
        if 0 <= digit < 10:
            return 1
        else:
            return 0

    sum = 0
    for number in range(10):
        sum += count_N(digit_number-1, digit-number)
    return sum


if __name__ == '__main__':
    pass
