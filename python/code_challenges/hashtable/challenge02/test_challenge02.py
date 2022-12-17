# Write your test here
from challenge02  import *
import pytest


def test_1():
    test = "ASAC                      is a       department          at LTUC. ASAC teaches programming in LTUC."
    actual = Repeated_Word(test)
    expected = 'ASAC'
    assert actual == expected

def test_1():
    test = "I am learning programming at ASAC."
    actual = Repeated_Word(test)
    expected = None
    assert actual == expected