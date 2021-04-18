def checkio(words: str) -> bool:
    counter = 0
    words_list = words.split(" ")
    for word in words_list:
        if word.isalpha():
            counter += 1
            if counter == 3:
                return True
        else:
            counter = 0
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True
    assert checkio("Hello World hello") == True
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
