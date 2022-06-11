def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """

    if text.find(begin) > text.find(end) and text.find(begin) != -1 and text.find(end) != -1:
        return ''
    else:
        if text.find(begin) >= 0:
            x1 = text.find(begin) + len(begin)
            res = text[x1:]

        else:
            res = text

        if res.find(end) > 0:
            x2 = res.find(end)
            print('x2 = ', x2)
            res2 = res[:x2]
            print('res2 = ', res)
            return res2
        else:
            return res


if __name__ == '__main__':
    print('Example:')
    print(between_markers('No [b]hi', '[b]', '[/b]'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    assert between_markers("No <hi> one", ">", "<") == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
