from codewars.level_8kyu.dnatornaconversion import dna_to_rna


def test_1():
    assert dna_to_rna("TTTT") == "UUUU"


def test_2():
    assert dna_to_rna("GCAT") == "GCAU"


def test_3():
    assert dna_to_rna("GACCGCCGCC") == "GACCGCCGCC"
