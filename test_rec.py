import pytest
import source.shapes as shapes
@pytest.fixture
def myrec():
    return shapes.Rectangle(10,20)

@pytest.fixture
def wierdrec():
   return shapes.Rectangle(5,6)

def test_perimeter(myrec):
    assert myrec.perimeter() == (10*2) + (20*2)


def test_not_equal(myrec, wierdrec):
    assert myrec != wierdrec