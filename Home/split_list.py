def split_list(items: list) -> list:
    l1 = []

    lenght_list = len(items)
    lenght_pair = lenght_list // 2

    if lenght_list % 2 == 0:
        for i in range(lenght_pair):
            l1.append(items[0])
            del items[0]
    elif lenght_list % 2 == 1:
        for i in range(lenght_pair + 1):
            l1.append(items[0])
            del items[0]

    return [l1, items]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
