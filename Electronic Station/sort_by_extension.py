from typing import List
import numpy as np

def sort_by_ext(files: List[str]) -> List[str]:
    files_data = []
    for i in files:
        num = i.count('.')
        res = i.split('.', -1)
        res_2 = ''.join(res[:num - 1]) + '.'.join(res[num - 1:])
        files_data.append(res_2)
    a = []
    for j in files_data:
        if j[0] == '.':
            j = '*' + j[0:]
        j = j.split('.')
        a.append(j)

    s = sorted(a, key=lambda x: (x[1], x[0]))
    final = []

    for k in s:
        if k[0] == '*':
            k[0] = ''
        k = '.'.join(k)
        final.append(k)

    return final


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    assert sort_by_ext(['.config', 'my.doc', '1.exe', '345.bin', 'green.bat', 'format.c', 'no.name.', 'best.test.exe']) == \
           ['.config', 'no.name.', 'green.bat', '345.bin', 'format.c', 'my.doc', '1.exe', 'best.test.exe']
    print("Coding complete? Click 'Check' to earn cool rewards!")
