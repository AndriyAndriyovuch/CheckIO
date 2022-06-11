from datetime import date


def days_diff(a, b):
    y1 = a[0]
    m1 = a[1]
    d1 = a[2]

    y2 = b[0]
    m2 = b[1]
    d2 = b[2]

    d1 = date(y1, m1, d1)
    d2 = date(y2, m2, d2)

    res = abs(d2 - d1)

    final = res.days
    return final


if __name__ == "__main__":
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
