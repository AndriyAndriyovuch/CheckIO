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
        b = b.replace('\\', '')
        if len(b) > 0 and b != '"null"':
            if b[0] == '"' and b[-1] == '"':
                b = b[1:]
                b = b[:-1]
        elif b == '"null"':
            pass
        res_values.append(b)

    key_values = []
    for key in keys:
        key = key.replace('"', '')
        key = key[:-1]
        key_values.append(key)

    ind = 0
    for i in range(len(key_values)):
        if res_values[ind] == 'true':
            res_values[ind] = True
            res[key_values[ind]] = res_values[ind]
            ind += 1
        elif res_values[ind] == 'false':
            res_values[ind] = False
            res[key_values[ind]] = res_values[ind]
            ind += 1
        elif len(res_values[ind]) == 0 or res_values[ind] == 'null':
            res_values[ind] = None
            res[key_values[ind]] = res_values[ind]
            ind += 1
        elif res_values[ind] == '"null"':
            res[key_values[ind]] = 'null'
            ind += 1
        else:
            try:
                res[key_values[ind]] = int(res_values[ind])
                ind += 1
            except ValueError:
                res[key_values[ind]] = res_values[ind]
                ind += 1
    res = dict(sorted(res.items()))
    return res


if __name__ == '__main__':
    print("Example:")
    print(yaml('name: "Bob Dylan"\n'
               'children: 6\n'
               'coding: "null" '))

    # {'alive': False, 'children': 6, 'name': 'Bob Dylan'}

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml('name: Alex Fox\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex Fox'}
    assert yaml('name: "Alex Fox"\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex Fox'}
    assert yaml('name: "Alex \\"Fox\\""\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'alive: false') == {'alive': False,
                                    'children': 6,
                                    'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding:') == {'children': 6,
                               'coding': None,
                               'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding: null') == {'children': 6,
                                    'coding': None,
                                    'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding: "null" ') == {'children': 6,
                                       'coding': 'null',
                                       'name': 'Bob Dylan'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
