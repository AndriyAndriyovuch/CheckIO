from typing import List


def letter_queue(commands: List[str]) -> str:
    final = []
    for i in commands:
        com_1 = i.split()

        if com_1[0] == "PUSH":
            final.append(com_1[1])
        elif com_1[0] == "POP":
            if len(final) > 0:
                del final[0]
            else:
                pass

    final = ''.join(final)
    return final


if __name__ == '__main__':
    print("Example:")
    print(letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert letter_queue(['PUSH A',
                         'POP',
                         'POP',
                         'PUSH Z',
                         'PUSH D',
                         'PUSH O',
                         'POP',
                         'PUSH T']) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")
