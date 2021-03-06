def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) > 0:
        a = 0
        sum = []
        for i in array:
            if a + 1 <= len(array):
                sum.append(array[a])
                a = a + 2

        ind = 0
        res = 0

        for i in sum:
            if ind + 1 <= len(sum):
                res = res + sum[ind]
                ind = ind + 1

        final = res * array[-1]
        return final
    else:
        return 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
