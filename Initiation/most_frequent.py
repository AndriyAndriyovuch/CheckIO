def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    index = 0
    list_cnt = 0
    res = None
    while index + 1 <= len(data):
        keyword = data[index]
        cnt = data.count(keyword)
        index = index + 1
        if cnt >= list_cnt:
            list_cnt = cnt
            res = keyword
    return res


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")
