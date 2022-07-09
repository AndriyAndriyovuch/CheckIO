def checkio(line1: str, line2: str) -> str:
    l1 = line1.split(sep=",")
    l2 = line2.split(sep=",")

    res = []

    for i in l1:
        if i in l2:
            res.append(i)

    res = sorted(res)
    final = ",".join(res)

    return final


if __name__ == '__main__':
    print("Example:")
    print(checkio('one,two,three','four,five,one,two,six,three'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
                   'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
