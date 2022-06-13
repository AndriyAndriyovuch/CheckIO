def beginning_zeros(number: str) -> int:
    check = list(number)

    sum = 0

    for i in check:
        if i == '0':
            sum = sum + 1
        else:
            break
    return sum


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('0000000100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")
