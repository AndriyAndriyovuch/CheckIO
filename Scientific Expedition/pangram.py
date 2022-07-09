def check_pangram(text):
    '''
        is the given text is a pangram.
    '''
    res_1 = text.lower()
    for i in res_1:
        if i.isalpha():
            pass
        else:
            res_1 = res_1.replace(i, '')

    final = set(res_1)

    if len(final) == 26:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_pangram("The quick brown fox jumps over the lazy dog."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')
