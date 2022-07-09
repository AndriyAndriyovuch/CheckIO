def goes_after(word: str, first: str, second: str) -> bool:
    res_1 = word.find(first)
    res_2 = word.find(second)
    if res_2 - res_1 == 1 and res_1 != -1 and res_2 != -1:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Example:")
    print(goes_after("almaz","r","a"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after("world", "w", "o") == True
    assert goes_after("world", "w", "r") == False
    assert goes_after("world", "l", "o") == False
    assert goes_after("panorama", "a", "n") == True
    assert goes_after("list", "l", "o") == False
    assert goes_after("", "l", "o") == False
    assert goes_after("list", "l", "l") == False
    assert goes_after("world", "d", "w") == False
    assert goes_after("transport", "r", "t") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
