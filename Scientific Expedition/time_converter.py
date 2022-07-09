def time_converter(time):
    time_res = time.split(sep=':')

    hours = int(time_res[0])
    minutes = time_res[1]

    if hours > 12:
        daytime = 'p.m.'
        hours -= 12
    elif hours == 12:
        daytime = 'p.m.'
    elif hours == 0:
        hours = 12
        daytime = 'a.m.'
    else:
        daytime = 'a.m.'

    return f'{hours}:{minutes} {daytime}'


if __name__ == '__main__':
    print("Example:")
    print(time_converter('00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert time_converter('12:30') == '12:30 p.m.'
    # assert time_converter('09:00') == '9:00 a.m.'
    # assert time_converter('23:15') == '11:15 p.m.'
    # print("Coding complete? Click 'Check' to earn cool rewards!")
