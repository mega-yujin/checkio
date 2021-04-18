def safe_pawns(pawns: set) -> int:
    indexes = set()
    counter = 0
    for pow in pawns:
        row = int(pow[1]) - 1
        col = ord(pow[0]) - 97
        indexes.add((row, col))

    for i in indexes:
        if (i[0]-1, i[1]-1) in indexes or (i[0]-1, i[1]+1) in indexes:
            counter += 1

    return counter


# print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
