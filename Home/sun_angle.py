from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    time_h = int(time[0] + time[1]) * 60
    time_m = int(time[3] + time[4])
    check_time = time_h + time_m

    if 360 <= check_time <= 1080:
        one_angle = (1080 - 360) / 180
        angle = (check_time - 360) / one_angle
        return angle
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:02"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
