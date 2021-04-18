def backward_string(val: str) -> str:
    reversed_val = str()
    for i in range(len(val) - 1, -1, -1):
        reversed_val += val[i]
    return reversed_val


def backward_string_2(val: str) -> str:
    reversed_val = str()
    for i in reversed(list(val)):
        reversed_val += i
    return reversed_val


def backward_string_3(val: str) -> str:
    return val[::-1]


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))
    print(backward_string_2('val'))
    print(backward_string_3('val'))
