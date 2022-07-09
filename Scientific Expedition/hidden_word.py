import re
import random

def checkio(text, word):
    res = text.split()

    c = re.sub(':', '\n', text)
    a = re.sub('\\n', '=', c)
    b = re.sub(' ', '', a)


    try:
        iter = [(m.start(0), m.end(0)) for m in re.finditer(word, b)]

        str_num = 1
        a2 = 0
        b2 = 0
        while True:
            w1 = re.search('=', b)
            index = w1.start()
            b = b[0 : index : ] + b[index + 1 : :]
            if iter[0][0] > index:
                str_num += 1
                a2 = iter[0][0] - index
                b2 = iter[0][1] - index - 1
            else:
                break
        res = [str_num, a2, str_num, b2]
        return res
    except IndexError:
        word_list = []
        for _ in word:
            word_list.append(_)

        text_list = b.split(sep='=')
        print(text_list)
        a_lst = []
        for let in word_list:
            ind = 1
            let_index = 0
            for _ in text_list:
                for p in _:
                    if p == '=':
                        ind += 1
                        let_index = 0
                    if p == let:
                        a_lst.append([ind, let_index])
                    else:
                        let_index += 1
            a_lst.append([1, -1111111111])
        # def take_index(smth):
        #     return smth[1]
        # a_lst.sort(key=take_index)
        return a_lst
















#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir"))# == [2, 14, 2, 16])
#     assert checkio("""
# DREAMING of apples on a wall,
# And dreaming often, dear,
# I dreamed that, if I counted all,
# -How many would appear?""", "ten") == [2, 14, 2, 16]
#     assert checkio("""He took his vorpal sword in hand:
# Long time the manxome foe he sought--
# So rested he by the Tumtum tree,
# And stood awhile in thought.
# And as in uffish thought he stood,
# The Jabberwock, with eyes of flame,
# Came whiffling through the tulgey wood,
# And burbled as it came!""", "noir") == [4, 16, 7, 16]
# print("Coding complete? Click 'Check' to earn cool rewards!")
