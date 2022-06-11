def frequency_sort(items):
    # your code here
    items_dict = dict.fromkeys(items, 0)

    for i in items_dict:
        cnt = items.count(i)
        items_dict[i] = cnt

    res_list = sorted(items_dict.items(), key=lambda kv: (kv[1]), reverse=True)
    res_dict = dict(res_list)

    final_list = []
    for k in res_dict:
        for i in range(res_dict[k]):
            final_list.append(k)

    return final_list


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4, 0, 3]))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    # assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    # assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    # assert list(frequency_sort([])) == []
    # assert list(frequency_sort([1])) == [1]
    # print("Coding complete? Click 'Check' to earn cool rewards!")
