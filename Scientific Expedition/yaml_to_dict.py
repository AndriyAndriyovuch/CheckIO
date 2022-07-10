def yaml(a):
    a = a.split()
    keys = []
    values = []

    res = {}
    value_compile = []

    for i in a:
        if i[-1] == ':':
            if len(value_compile) > 0:
                values.append(value_compile)
            keys.append(i)
            value_compile = []
        else:
            value_compile.append(i)
    values.append(value_compile)

    res_values = []
    for val in values:
        b = ' '.join(val)
        res_values.append(b)

    key_values = []
    for key in keys:
        key = key[:-1]
        key_values.append(key)

    ind = 0
    for i in range(len(key_values)):
        try:
            res[key_values[ind]] = int(res_values[ind])
            ind += 1
        except ValueError:
            res[key_values[ind]] = res_values[ind]
            ind += 1

    return res


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex Fox
    age: 12
    
    class: 12b"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
    age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
    age: 12

    class: 12b""") == {'age': 12,
                       'class': '12b',
                       'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
