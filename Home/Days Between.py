import datetime


def days_diff(a, b):
    date_1 = datetime.date(a[0], a[1], a[2])
    date_2 = datetime.date(b[0], b[1], b[2])
    days_between = date_1 - date_2
    return abs(days_between.days)


if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
