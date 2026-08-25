import pytest
import time
from source import myfunc

def test_add():
    assert myfunc.add(2, 3) == 5 

def test_rollingAvg():
    res = myfunc.rollingAvg([1, 2, 3, 4, 5, 6], 3)
    assert res == [2.0, 3.0, 4.0, 5.0]

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    res = myfunc.add(2,3)
    assert res == 5

@pytest.mark.skip(reason="Skipping this test for now")
def test_add():
    assert myfunc.add(2, 3) == 5


@pytest.mark.xfail(reason="This test is expected to fail")
def test_rollingAvg():
    res = myfunc.rollingAvg([1, 2, 3, 4, 5, 6], 3)
    assert res == [2.0, 3.0, 4.0, 5.0]