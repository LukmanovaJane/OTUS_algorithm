def count_characters(string: str) -> str:
    """ Count characters in given string

    Examples:
        >>> count_characters('abcdefghijklmnoprstuvwxyz')
        '25'
    """
    counter = 0
    for char in string:
        counter += 1
    return str(counter)


if __name__ == '__main__':
    pass
