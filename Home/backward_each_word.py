from unittest import result


def backward_string_by_word(text: str) -> str:
    lst_1 = []
    a = ''

    for i in text:
        check = i.isalpha()
        if check == True:
            a = a + i
        elif check == False:
            lst_1.append(a)
            a = ''
            lst_1.append(i)
    lst_1.append(a)

    rev_list = []

    for o in lst_1:
        check_2 = o.isalpha()
        if check_2 == True:
            res = o[::-1]
            rev_list.append(res)
        if check_2 == False:
            rev_list.append(o)

    result = ''.join(rev_list)

    return result


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word('welcome to a game'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
