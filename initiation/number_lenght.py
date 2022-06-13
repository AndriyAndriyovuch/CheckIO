def number_length(a: int) -> int:
    b = 10
    if a >= 10:
        res = 2
        while a // b >= 10:
            res = res + 1
            b = b * 10
        return res
    else:
        return 1



if __name__ == "__main__":
    print("Example:")
    print(number_length(471111111111115))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
