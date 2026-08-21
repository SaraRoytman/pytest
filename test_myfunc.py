import pytest
from source import myfunc

def test_add():
    assert myfunc.add(2, 3) == 5