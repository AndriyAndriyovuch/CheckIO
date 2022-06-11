def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    a = text.find(begin)

    text_lst = list(text)

    while a >= 0:
        del (text_lst[a])
        a = a - 1

    while text_lst[-1] != end:
        del (text_lst[-1])

    del (text_lst[-1])

    result = ''.join(text_lst)

    return result


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
