def checkio(number: int) -> int:
    numbers = [i for i in str(number)]
    result = int(numbers[0])
    for num in numbers[1:]:
        if num != '0':
            result *= int(num)
    return result


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    assert checkio(00000) == 0
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
