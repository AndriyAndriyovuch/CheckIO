def nearest_value(values: set, one: int) -> int:
    lst = list(values)
    lst.sort()

    if one <= lst[0]:
        return lst[0]
    elif one >= lst[-1]:
        return lst[-1]
    else:

        lst.append(one)
        lst.sort()
        index = 0
        while lst[index] != one:
            index = index + 1
        n1 = lst[index - 1]
        n2 = lst[index + 1]
        if one - n1 == one or n2 - one == one:
            return one
        elif one - n1 <= n2 - one:
            return n1
        elif one - n1 > n2 - one:
            return n2


if __name__ == "__main__":
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    # assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    # assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({5}, 5) == 5
    assert nearest_value({5}, 7) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")
