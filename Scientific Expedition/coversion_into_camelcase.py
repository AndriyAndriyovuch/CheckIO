def to_camel_case(name: str) -> str:
    camel_text = name.split(sep='_')

    res = []
    for i in camel_text:
        b = i.capitalize()
        res.append(b)

    final = ''.join(res)
    return final


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case("this_function_is_empty"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
