from codewars.level_8kyu.school_paperwork import paperwork


def test_1():
    # "Failed at Paperwork(5,5)"
    assert paperwork(5, 5) == 25


def test_2():
    # "Failed at Paperwork(-5,5)"
    assert paperwork(-5, 5) == 0


def test_3():
    # "Failed at Paperwork(5,-5)"
    assert paperwork(5, -5) == 0


def test_4():
    # "Failed at Paperwork(-5,-5)"
    assert paperwork(-5, -5) == 0


def test_5():
    # "Failed at Paperwork(5,0)"
    assert paperwork(5, 0) == 0
