# 'Returned value should be the value left over after dividing as much as possible.'
from codewars.level_8kyu.find_the_remainder import remainder


def test_1():
    assert remainder(17, 5) == 2


def test_2():
    assert remainder(13, 72) == remainder(72, 13)


def test_3():
    assert remainder(1, 0) is None


def test_4():
    assert remainder(0, 0) is None


def test_5():
    assert remainder(0, 1) is None


def test_6():
    assert remainder(-1, 0) == 0


def test_7():
    assert remainder(0, -1) == 0


def test_8():
    assert remainder(-13, -13) == 0


def test_9():
    assert remainder(-60, 340) == -20


def test_10():
    assert remainder(60, -40) == -20
