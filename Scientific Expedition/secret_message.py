def find_message(message: str) -> str:
    text_list = []

    for word in message:
        text_list.append(word)

    res = []

    for letter in text_list:
        if letter.isupper():
            res.append(letter)

    final = ''.join(res)
    return final


if __name__ == '__main__':
    print("Example:")
    print(find_message(('How are you? Eh, ok. Low or Lower? '
                        + 'Ohhh.')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_message(('How are you? Eh, ok. Low or Lower? '
                         + 'Ohhh.')) == 'HELLO'
    assert find_message('hello world!') == ''
    assert find_message('HELLO WORLD!!!') == 'HELLOWORLD'
    print("Coding complete? Click 'Check' to earn cool rewards!")
