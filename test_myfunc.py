import pytest
from source import myfunc

def test_add():
    assert myfunc.add(2, 3) == 5 

def test_rollingAvg():
    res = myfunc.rollingAvg([1, 2, 3, 4, 5, 6], 3)
    assert res == [2.0, 3.0, 4.0, 5.0]
