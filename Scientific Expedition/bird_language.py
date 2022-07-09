def translate(text: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'i', 'u', 'y']
    text_list = []

    for i in text:
        text_list.append(i)

    vowel_ind = 0

    for j in text_list:
        if j in vowels:
            del text_list[vowel_ind + 1]
            del text_list[vowel_ind + 1]
            vowel_ind += 1
        elif j == " ":
            vowel_ind += 1
        elif j not in vowels:
            del text_list[vowel_ind + 1]
            vowel_ind += 1

    res = ''.join(text_list)

    return res


if __name__ == "__main__":
    print("Example:")
    print(translate("hoooowe yyyooouuu duoooiiine"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to earn cool rewards!")
