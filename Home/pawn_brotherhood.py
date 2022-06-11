def safe_pawns(pawns: set) -> int:
    cnt = 0

    for i in pawns:
        a = ord(i[0])
        b = i[1]

        a1 = chr(a + 1)
        b1 = str(int(b) - 1)

        a2 = chr(a - 1)
        b2 = str(int(b) - 1)

        res1 = str(a1 + b1)
        res2 = str(a2 + b2)

        if res1 in pawns or res2 in pawns:
            cnt += 1
        else:
            pass
    return cnt


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
