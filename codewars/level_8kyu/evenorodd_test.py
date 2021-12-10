from codewars.level_8kyu.evenorodd import even_or_odd


def test_1():
    assert even_or_odd(2) == "Even"


def test_2():
    assert even_or_odd(1) == "Odd"


def test_3():
    assert even_or_odd(0) == "Even"


def test_4():
    assert even_or_odd(1545452) == "Even"


def test_5():
    assert even_or_odd(7) == "Odd"


def test_6():
    assert even_or_odd(78) == "Even"


def test_7():
    assert even_or_odd(17) == "Odd"


def test_8():
    assert even_or_odd(74156741) == "Odd"


def test_9():
    assert even_or_odd(100000) == "Even"


def test_10():
    assert even_or_odd(-123) == "Odd"


def test_11():
    assert even_or_odd(-456) == "Even"
