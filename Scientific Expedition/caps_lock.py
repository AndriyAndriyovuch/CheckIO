def caps_lock(text: str) -> str:
    res = []
    for let in text:
        res.append(let)

    final = []
    check = 0
    for i in res:
        if i.isalpha():
            if i.islower():
                if i == 'a':
                    i = ''
                    check += 1
                    pass
                if check == 0:
                    final.append(i)
                elif check % 2 == 1 and i != '':
                    if i.isupper():
                        final.append(i.lower())
                    elif i.islower():
                        final.append(i.upper())
                elif check % 2 == 0 and i != '':
                    if i.isupper():
                        final.append(i.upper())
                    elif i.islower():
                        final.append(i.lower())
            else:
                final.append(i)
        else:
            final.append(i)

    result = ''.join(final)

    return result


if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")
