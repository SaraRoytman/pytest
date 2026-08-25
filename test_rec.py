import pytest
import source.shapes as shapes


def test_perimeter(myrec):
    assert myrec.perimeter() == (10*2) + (20*2)


def test_not_equal(myrec, wierdrec):
    assert myrec != wierdrec