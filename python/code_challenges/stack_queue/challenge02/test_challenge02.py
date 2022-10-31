import pytest
from challenge02 import *


def test_1():

    actual = isValid("()[]{}")
    expected = True

    assert actual == expected


def test_2():

    actual = isValid("(])[]{}")
    expected = False

    assert actual == expected
    
def test_3():

    actual = isValid("[(hello)()]")
    expected = True

    assert actual == expected
