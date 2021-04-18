def sun_angle(time):
    minutes = int(time[:2]) * 60 + int(time[3:])
    if minutes < 360 or minutes > 1080:
        return "I don't see the sun!"
    else:
        return (minutes - 360) * 180 / 720


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
