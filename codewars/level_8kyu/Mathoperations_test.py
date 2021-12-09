from codewars.level_8kyu.Mathoperations import ice_brick_volume


def test_1():
    assert ice_brick_volume(1, 10, 2) == 16


def test_2():
    assert ice_brick_volume(5, 30, 7) == 1150
