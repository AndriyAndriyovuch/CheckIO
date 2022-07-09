def from_camel_case(name: str) -> str:
    res = []
    for i in name:
        if i.isupper():
            res.append('_')
            i = i.lower()
            res.append(i)
        else:
            res.append(i)

    if res[0] == '_':
        del res[0]

    final = ''.join(res)
    return final


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
