# Write here the code challenge solution
from collections import deque

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, source, target, weight = 0):
        if source not in self.edges:
            self.edges[source] = [target]
        else:
            self.edges[source].append(target)
        self.distances[(source, target)] = weight

    def breadth_first(self, start_node):


        '''
        A method that take a value as argument, then traverse through the graph using Breadth First way starting from the inputted value, 
        and appending all the visited nodes values in a returned array
        '''



        visited = []
        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                neighbors = self.edges.get(node, [])
                for neighbor in neighbors:
                    queue.append(neighbor)
        return visited

graph = Graph()

# graph.add_node('a')
# graph.add_node('b')
# graph.add_node('c')
# graph.add_node('d')
# graph.add_edge('a', 'b', 5)
# graph.add_edge('a', 'c', 2)
# graph.add_edge('b', 'd', 1)
# graph.add_edge('b', 'c', 3)
# graph.add_edge('c', 'a', 7)

# print(graph.breadth_first('a'))