def checkio(text: str) -> str:
    res_1 = text.lower()
    res_list = []
    for i in res_1:
        if i.isalpha():
            res_list.append(i)

    set_1 = sorted(set(res_list))

    dict_1 = dict.fromkeys(set_1, 0)

    for i in res_list:
        if i in dict_1.keys():
            dict_1[i] += 1

    res = dict(sorted(dict_1.items(), key=lambda item: item[1], reverse=True))
    final = list(res.keys())

    return final[0]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
