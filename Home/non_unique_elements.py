def checkio(data: list) -> list:
    check = []
    for i in data:
        a = data.count(i)
        check.append(a)

    final = []
    for k in check:
        if k > 1:
            a = check.index(k)
            final.append(data[a])
            check[a] = 1
    return final


if __name__ == "__main__":
    print(checkio(
        [1, 2, 3, 1, 3]))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
