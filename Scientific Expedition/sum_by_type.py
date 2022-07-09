from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    str_list = []
    int_list = []
    for i in items:
        if isinstance(i, str):
            str_list.append(i)
        elif isinstance(i, int):
            int_list.append(i)
        else:
            pass

    res_str = ''
    for i in str_list:
        res_str += i

    res_int = 0
    for i in int_list:
        res_int += i
    return (res_str, res_int)


if __name__ == "__main__":
    print("Example:")
    print(sum_by_types(["size", 12, "in", 45, 0]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_by_types([]) == ("", 0)
    assert sum_by_types([1, 2, 3]) == ("", 6)
    assert sum_by_types(["1", 2, 3]) == ("1", 5)
    assert sum_by_types(["1", "2", 3]) == ("12", 3)
    assert sum_by_types(["1", "2", "3"]) == ("123", 0)
    assert sum_by_types(["size", 12, "in", 45, 0]) == ("sizein", 57)
    print("Coding complete? Click 'Check' to earn cool rewards!")
