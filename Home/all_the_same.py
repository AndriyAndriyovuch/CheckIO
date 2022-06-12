from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    ind_2 = 1

    res = True
    for i in elements:
        try:
            if i == elements[ind_2]:
                res = True
                ind_2 += 1
            else:
                res = False
                break
        except IndexError:
            return res
    return res


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
