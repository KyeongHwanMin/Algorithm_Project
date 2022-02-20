from codewars.level_8kyu.abbreviateatwowordname import abbrev_name


def test_1():
    assert abbrev_name("Sam Harris") == "S.H"


def test_2():
    assert abbrev_name("patrick feenan") == "P.F"

def test_3():
    assert abbrev_name("Evan C") == "E.C"


def test_4():
    assert abbrev_name("P Favuzzi") == "P.F"


def test_5():
    assert abbrev_name("David Mendieta") == "D.M"
