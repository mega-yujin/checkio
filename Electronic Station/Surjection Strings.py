# You need to check that the String A is isometric to the String B.
# This means that a character from String A can become a match for characters from String B.
#
# One character from String A can correspond only to one character from String B.
# Two or more characters of String B can correspond to one character of String A.
# Input: Two arguments. String A and String B.
#
# Output: Boolean.
#
# Example:
# isometric_strings('add', 'egg') == True
# isometric_strings('foo', 'bar') == False
# isometric_strings('', '') == True

def isometric_strings(str1: str, str2: str) -> bool:
    return len(set(zip(str1, str2))) == len(set(str1))


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('add', 'egg'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
