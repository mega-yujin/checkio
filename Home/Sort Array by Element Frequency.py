def frequency_sort(items):
    return sorted(items, key=lambda x: (-items.count(x), items.index(x)))


# def frequency_sort(items):
#     sorted_items = list()
#     elements_freq = dict()
#     for i in items:
#         elements_freq[i] = items.count(i)
#
#     for i in elements_freq:
#         sorted_items.append(i)
#     return elements_freq

# def frequency_sort(items):
#     frequency = collections.Counter(items)
#     sorted_items = sorted(items, key=lambda x: (-frequency[x], x))
#     # items.sort(key=lambda x: (-frequency[x], x))
#     return sorted_items


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
    # assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    # assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    # assert list(frequency_sort([])) == []
    # assert list(frequency_sort([1])) == [1]
    # print("Coding complete? Click 'Check' to earn cool rewards!")
