def is_acceptable_password(password: str) -> bool:
    unique_symbols = len(set(password))
    if len(password) > 9:
        if password.lower().find('password') == -1 and unique_symbols >= 3:
            return True
        else:
            return False
    return len(password) > 6 \
           and any(i.isdigit() for i in password) \
           and not password.isdigit() \
           and password.lower().find('password') == -1 \
           and unique_symbols >= 3


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('aaaaaabb1'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("aaaaaaabbaaaaaaaab") == False
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    assert is_acceptable_password('aaaaaa1') == False
    assert is_acceptable_password('aaaaaabbbbb') == False
    assert is_acceptable_password('aaaaaabb1') == True
    assert is_acceptable_password('abc1') == False
    assert is_acceptable_password('abbcc12') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
