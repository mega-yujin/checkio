def end_zeros(num: int) -> int:
    if num == 0:
        return 1
    else:
        zeros_count = 0
        while num % 10 == 0:
            zeros_count += 1
            num //= 10
        return zeros_count


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
