from sci_calc import *
import pytest

@pytest.mark.skip("Work in progress")
def test_find_sqrt():
    assert find_sqrt(100) == 10.0

def test_find_ceil():
    assert find_ceil(3.14) == 4


