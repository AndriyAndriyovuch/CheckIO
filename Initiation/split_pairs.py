def split_pairs(a):
    lst = list(a)

    if len(lst) % 2 == 1:
        lst.append('_')

    result = []

    while len(lst) > 0:
        pair = lst[0] + lst[1]
        result.append(pair)
        del lst[0]
        del lst[0]

    return result


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
