# Write your test here
import pytest
from challenge01 import *




def test1():


    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_edge('a', 'b', 5)
    graph.add_edge('a', 'c', 2)
    graph.add_edge('b', 'd', 1)
    graph.add_edge('b', 'c', 3)
    graph.add_edge('c', 'a', 7)

    
    actual = graph.breadth_first('a')
    expected = ['a', 'b', 'c', 'd']
    assert actual == expected



def test2():


    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 1)
    graph.add_edge(2, 3, 1)
    graph.add_edge(2, 4, 1)
    graph.add_edge(3, 4, 1)
    
    actual = graph.breadth_first(1)
    expected = [1, 2, 3, 4]
    assert actual == expected

