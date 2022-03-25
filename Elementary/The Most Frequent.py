# You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.
# It can be only one.
#
# Input: non empty list of strings.
#
# Output: a string.
#
# Example:
# most_frequent([
#     'a', 'b', 'c',
#     'a', 'b',
#     'a'
# ]) == 'a'
# most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'

def most_frequent(data: list) -> str:
    counter = dict()
    for i in data:
        if i not in counter.keys():
            counter[i] = 1
        else:
            counter[i] += 1
    return max(counter.items(), key= lambda i: i[1])[0]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))
    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")
