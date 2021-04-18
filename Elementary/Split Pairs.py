def split_pairs(a):
    pairs = []
    if len(a) == 0:
        return a
    elif len(a) % 2 == 0:
        for i in range(0, len(a), 2):
            pairs.append(a[i: i+2])
        return pairs
    else:
        for i in range(0, len(a)-1, 2):
            pairs.append(a[i: i+2])
        pairs.append(a[-1] + '_')
        return pairs


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
