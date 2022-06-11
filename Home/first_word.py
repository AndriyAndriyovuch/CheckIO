def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """

    if '.' in text:
        text = text.replace('.', ' ')
    elif ',' in text:
        text = text.replace(',', ' ')

    lst = text.split()
    res = []

    for i in lst:
        if len(res) == 1:
            pass
        elif i.isalpha() or "'" in i:
            res.append(i)
        else:
            pass

    final = ''.join(res)

    return final


if __name__ == "__main__":
    print("Example:")
    print(first_word("... and so on ..."))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
