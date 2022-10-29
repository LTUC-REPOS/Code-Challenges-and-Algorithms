import pytest
from challenge01 import *


def test_1():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)

    actual =  q.peek()
    expected = 1
    assert actual == expected


def test_2():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)

    actual =  q.pop() + q.pop()
    expected = 3
    assert actual == expected