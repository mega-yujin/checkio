from typing import List


def extension(file):
    index = file.rfind('.')
    if index == 0:
        key = file
    elif index == len(file) - 1:
        key = file
    else:
        key = '~' + file[index + 1:] + file[:index]
    return key


def sort_by_ext(files: List[str]) -> List[str]:
    return sorted(files, key=extension)


if __name__ == '__main__':
    print("Example:")
    # print(sort_by_ext(['1.cad', '1.bat', '1.aa']))
    # print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']))
    print(sort_by_ext([".config","my.doc","1.exe","345.bin","green.bat","format.c","no.name.","best.test.exe"]))
    print(sort_by_ext(["1.cad","2.bat","1.aa","1.bat"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext([".config","my.doc","1.exe","345.bin","green.bat","format.c","no.name.","best.test.exe"]) == [".config","no.name.","green.bat","345.bin","format.c","my.doc","1.exe","best.test.exe"]
    assert sort_by_ext(["1.cad","2.bat","1.aa","1.bat"]) == ["1.aa","1.bat","2.bat","1.cad"]
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")
