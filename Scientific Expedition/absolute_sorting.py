def checkio(values: list) -> list:
    a = []

    for i in values:
        i = abs(i)
        a.append(i)

    res = zip(a, values)
    sort_res = sorted(res)

    a = zip(*sort_res)
    a, values = [list(j) for j in a]

    return values


if __name__ == '__main__':
    print("Example:")
    print(checkio([-20, -5, 10, 15]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
    print("Coding complete? Click 'Check' to earn cool rewards!")
