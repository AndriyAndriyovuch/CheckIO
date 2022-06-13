def backward_string(val: str) -> str:
    if not len(val) == 0:
        res = val[-1]
        a = 2
        b = -2
        while a <= len(val):
            res = res + val[b]
            b = b - 1
            a = a + 1
        return(res)
    else:
        return ""

if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")