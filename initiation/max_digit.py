def max_digit(number: int) -> int:

    if not number == 0:
        lst = []
        a = 10
        check = number
        while check > 0:
            lst.append(check % 10)
            check = check // 10
            a = a * 10
        solution = max(lst)
        return solution
    else:
        return 0

if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
