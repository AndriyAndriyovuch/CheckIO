def date_time(time: str) -> str:
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']

    time = time.replace('.', ' ')
    time = time.replace(':', ' ')

    time_list = time.split()

    day = int(time_list[0])
    month = int(time_list[1]) - 1
    year = int(time_list[2])
    hour = int(time_list[3])
    minute = int(time_list[4])

    if hour == 1:
        hour_str = 'hour'
    else:
        hour_str = 'hours'

    if minute == 1:
        minute_str = 'minute'
    else:
        minute_str = 'minutes'

    res = f'{day} {month_list[month]} {year} year {hour} {hour_str} {minute} {minute_str}'

    return res


if __name__ == "__main__":
    print("Example:")
    print(date_time("20.11.199 01:01"))

    # # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert (
    #         date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    # ), "Millenium"
    # assert (
    #         date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    # ), "Victory"
    # assert (
    #         date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    # ), "Somebody was born"
    # print("Coding complete? Click 'Check' to earn cool rewards!")
