# Write your test here
from challenge01  import *
import pytest


def test_1():
    tree = Tree()
    input = [5,3,6,2,4,None,7]
    k = 28
    for x in input:
        tree.insert(x)
    
    actual = findTarget(tree.root,k)
    expected = False

    assert actual == expected


def test_2():
    tree = Tree()
    input = [5,3,6,2,4,None,7]
    k = 8
    for x in input:
        tree.insert(x)
    
    actual = findTarget(tree.root,k)
    expected = True

    assert actual == expected