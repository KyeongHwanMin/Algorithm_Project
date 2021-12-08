from codewars.level_8kyu.string_repeat import repeat_str


def test_1():
    assert repeat_str(4, 'a') == 'aaaa'


def test_2():
    assert repeat_str(3, 'hello ') == 'hello hello hello '


def test_3():
    assert repeat_str(2, 'abc') == 'abcabc'
