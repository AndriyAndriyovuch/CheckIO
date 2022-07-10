def words_order(text: str, words: list) -> bool:
    text = text.split()
    ch_1 = set(words)

    if len(ch_1) < len(words):
        return False
    else:
        res_list = []

        for i in text:
            if i in words:
                res_list.append(i)

        if len(words) <= len(res_list):
            res_list = sorted(set(res_list), key=res_list.index)
            res_list = list(res_list)
            ind = 0
            res = False
            for val in res_list:
                if val == words[ind]:
                    res = True
                    ind += 1
                else:
                    return False
            return res
        else:
            return False


if __name__ == "__main__":
    print("Example:")
    print(words_order("hi world im here", ["world", "im", "here"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order("hi world im here", ["world", "here"]) == True
    assert words_order("hi world im here", ["here", "world"]) == False
    assert words_order("hi world im here", ["world"]) == True
    assert words_order("hi world im here", ["world", "here", "hi"]) == False
    assert words_order("hi world im here", ["world", "im", "here"]) == True
    assert words_order("hi world im here", ["world", "hi", "here"]) == False
    assert words_order("hi world im here", ["world", "world"]) == False
    assert words_order("hi world im here", ["country", "world"]) == False
    assert words_order("hi world im here", ["wo", "rld"]) == False
    assert words_order("", ["world", "here"]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
