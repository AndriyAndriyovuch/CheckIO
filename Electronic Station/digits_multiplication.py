def checkio(number: int) -> int:
    number = str(number)
    num_list = []
    for i in number:
        if i != '0':
            num_list.append(i)

    res = 1
    for g in num_list:
        g = int(g)
        res = g * res
    return res


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
