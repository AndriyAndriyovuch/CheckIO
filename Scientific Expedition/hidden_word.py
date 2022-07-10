# import re
# import random
#
# def checkio(text, word):
#     res = text.split()
#
#     c = re.sub(':', '\n', text)
#     a = re.sub('\\n', '=', c)
#     b = re.sub(' ', '', a)
#
#
#     try:
#         iter = [(m.start(0), m.end(0)) for m in re.finditer(word, b)]
#
#         str_num = 1
#         a2 = 0
#         b2 = 0
#         while True:
#             w1 = re.search('=', b)
#             index = w1.start()
#             b = b[0 : index : ] + b[index + 1 : :]
#             if iter[0][0] > index:
#                 str_num += 1
#                 a2 = iter[0][0] - index
#                 b2 = iter[0][1] - index - 1
#             else:
#                 break
#         res = [str_num, a2, str_num, b2]
#         return res
#     except IndexError:
#         word_list = []
#         for _ in word:
#             word_list.append(_)
#
#         text_list = b.split(sep='=')
#         print(text_list)
#         a_lst = []
#         for let in word_list:
#             ind = 1
#             let_index = 1
#             for v in text_list:
#                 v += '='
#                 for p in v:
#                     if p == let:
#                         a_lst.append([let_index, ind])
#                         let_index += 1
#                     elif p == '=':
#                         ind += 1
#                         let_index = 1
#                     else:
#                         let_index += 1
#             # a_lst.append([1, -1111111111])
#
#         a_lst = sorted(a_lst)
#
#         check = 0
#         ind1 = 1
#         for key in a_lst:
#             compare = a_lst[ind1]
#             if (key[1] + 1) == compare[1] and key[0] == compare[0]:
#                 check += 1
#                 ind1 += 1
#             elif (key[1] + 1) != compare[1]:
#                 check = 0
#                 ind1 += 1
#             if check == len(word_list):
#                 return key
#

        # word_list = []
        # for _ in word:
        #     word_list.append(_)
        #
        # text_list = b.split(sep='=')
        # print(text_list)
        # str_ind = 0
        # let_ind = 0
        # word_ind = 0
        # #
        # # while True:
        # #     check = 0
        # #     k = text_list[str_ind][let_ind]
        # #     n = word_list[word_ind]
        #     if k == n:
        #         str_ind += 1
        #         let_ind += 1
        #         word_ind += 1
        #         check += 1
        #     elif k != n:
        #         let_ind += 1
        #         check = 0
        #     elif IndexError:
        #         str_ind += 1
from itertools import zip_longest


def check_horizontals(text, word):
    """
    Search the word in the text by rows

    Args:
        text -- A list of strings
        word -- our "hidden" word

    Return:
        The row and column of the first letter of the word
    """
    for i, line in enumerate(text):
        if word in line:
            return i, line.index(word)
    return None, None


def checkio(text, word):
    """
    Search the "hidden" word in the text.

    Args:
        text -- Multiline string for search
        word -- our "hidden" word

    Return:
        The list with coordinates of the word
    """

    # normalize text in the matrix
    text = text.replace(" ", "").lower()
    data = text.split("\n")

    row, col = check_horizontals(data, word)
    if row is not None:
        return [row + 1, col + 1, row + 1, col + len(word)]

    # transpose text. zip_longest does not truncate rows.
    data = ("".join(row) for row in zip_longest(*data, fillvalue=""))

    row, col = check_horizontals(data, word)
    if row is not None:
        return [col + 1, row + 1, col + len(word), row + 1]

    raise ValueError("The rhyme does not contain the word.")
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
    assert checkio("""
DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")
