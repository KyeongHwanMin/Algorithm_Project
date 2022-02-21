from codewars.level_8kyu.countingsheep import count_sheeps


def test_1():
    # "There are 17 sheeps in total, not %s"
    array1 = [True, True, True, False,
              True, True, True, True,
              True, False, True, False,
              True, False, False, True,
              True, True, True, True,
              False, False, True, True];


    assert count_sheeps(array1) == 17