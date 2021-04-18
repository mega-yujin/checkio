def nearest_value(values: set, one: int) -> int:
    value = [0, float("inf")]
    values = sorted(values)
    for i in values:
        diff = abs(one - i)
        if diff < value[1]:
            value = [i, diff]
    return value[0]


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
    print(nearest_value({4, 8, 10, 11, 12, 17}, 9))
    print(nearest_value({4, 8, 10, 11, 12, 17}, 9))
    nearest_value({4, 8, 10, 11, 12, 17}, 9)

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    assert nearest_value([0, -2], -1) == -2
    print("Coding complete? Click 'Check' to earn cool rewards!")
