def checkio(words: str) -> bool:
    word_list = words.split()

    checklist = []
    for integ in word_list:
        try:
            check = int(integ)
            checklist.append(check)
        except ValueError:
            checklist.append(integ)

    if len(word_list) >= 3:
        check_final = 0
        for i in checklist:
            a = isinstance(i, str)
            if a:
                check_final = check_final + 1
                if check_final == 3:
                    return True
            else:
                check_final = 0
        if check_final >= 3:
            return True
        else:
            return False
    else:
        return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True
    assert checkio("He is 123 man") == False
    assert checkio("1 2 3 4") == False
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True
    assert checkio("Hi") == False
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
