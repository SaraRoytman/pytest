
import pytest
import source.shapes as shapes

@pytest.fixture
def myrec():
    return shapes.Rectangle(10,20)

@pytest.fixture
def wierdrec():
   return shapes.Rectangle(5,6)