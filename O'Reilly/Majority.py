def is_majority(items: list) -> bool:
    if len(items) != 0:
        true_counter = 0
        false_counter = 0
        for i in items:
            if i == 1:
                true_counter += 1
            else:
                false_counter += 1
        if true_counter > false_counter:
            return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
