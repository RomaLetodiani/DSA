# graph = [
#    0  1  2  3  4  5
# 0 [0, 0, 0, 0, 1, 1],
# 1 [0, 0, 1, 1, 1, 0],
# 2 [0, 1, 0, 1, 0, 0],
# 3 [0, 1, 1, 0, 1, 0],
# 4 [1, 1, 0, 1, 0, 0],
# 5 [1, 0, 0, 0, 0, 0]
# ]

# graph methods:

# __init__(N: int)              - makes graph with N vertices and it does not have any edges
# print_graph()                 - prints graph
# add_vertex(v)                 - adds vertex to the graph
# add_edge(v1: int, v2: int)    - adds edges between v1 and v2
# remove_edge(v1: int, v2: int) - removes edge between v1 and v2
# remove_vertex(v)              - removes vertex from graph
# num_edges()                   - returns number of edges
# get_neighbors(v: int)         - return neighbors of v
# contains(v)                   - checks if graph has v
# _get_index(v)                 - returns index of v


class adjacencyMatrixGraph:
    # O(V^2) if n > 0
    # O(1) if we dont have n
    def __init__(self, n)-> None:
        self.storage = [] # O(1)
        self.pairs = [] # O(1)
        for v in range(1, n+1): # O(V)
            self.add_vertex(v) # O(V)
        self.edges = 0 # O(1)


    # O(V^2)
    def print_graph(self) -> list[list[int]]:
        print('[') # O(1)
        for row in self.storage: # O(V^2)
            print(row)
        print(']') # O(1)

    # O(V)
    def add_vertex(self, v)-> None:
        if not self.storage: # O(1)
            self.storage.append([0]) # O(1)
            self.pairs.append([v, len(self.pairs)]) # O(1)
            return
        
        self.storage.append([0] * len(self.storage[0])) # O(V)
        self.pairs.append([v, len(self.pairs)]) # O(1)
        for row in self.storage: # O(V)
            row.append(0) # O(1)

    # O(V)
    def add_edge(self, v1: int, v2: int)-> None:
        if not self.contains(v1): # O(V)
            self.add_vertex(v1) # O(V)

        if not self.contains(v2): # O(V)
            self.add_vertex(v2) # O(V)

        index1 = self._get_index(v1) # O(V)
        index2 = self._get_index(v2) # O(V)

        if self.storage[index1][index2] != 1 and self.storage[index2][index1] != 1: # O(1)
            self.edges += 1 # O(1)


        self.storage[index1][index2] = 1 # O(1)
        self.storage[index2][index1] = 1 # O(1)


    # O(V)
    def remove_edge(self, v1: int, v2: int)-> None:
        if not self.contains(v1) or not self.contains(v2): # O(V)
            return
        index1 = self._get_index(v1) # O(V)
        index2 = self._get_index(v2) # O(V)

        if self.storage[index1][index2] == 1 or self.storage[index2][index1] == 1: # O(1)
            self.edges -= 1 # O(1)
    

        self.storage[index1][index2] = 0 # O(1)
        self.storage[index2][index1] = 0 # O(1)


    # O(V^2)
    def remove_vertex(self, v: int)-> None:
        if not self.contains(v): # O(V)
            return
        
        index = self._get_index(v) # O(V)
        for pair in self.pairs: # O(V)
            if pair[1] > index: # O(1)
                pair[1] -= 1 # O(1)

        for pair in self.pairs: # O(V)
            if pair[0] == v: # O(1)
                self.pairs.remove(pair) # O(V)

        for i in self.storage[index]: # O(V)
            self.edges -= i # O(1)

        self.storage.pop(index) # O(V)
        for row in self.storage: # O(V)
            row.pop(index) # O(V)

    # O(1)
    def num_edges(self)-> int:
        return self.edges # O(1)
    
    # Time  : O(V^2)
    # Space : O(V)
    def get_neighbors(self, v: int)-> list[list[int]]:
        if not self.contains(v): # O(V)
            return [] # O(1)
        
        neighbors = [] # O(1)
        neighborsIndexes = [] # O(1)
        index = self._get_index(v) # O(V)

        for i, n  in enumerate(self.storage[index]): # O(V)
            if n == 1: # O(1)
                neighborsIndexes.append(i) # O(1)

        for pair in self.pairs: # O(V)
            for i in neighborsIndexes: # O(V)
                if pair[1] == i: # O(1)
                    neighbors.append(pair[0]) # O(1)

        return neighbors
    
    # O(V)
    def contains(self, v)-> bool:
        for pair in self.pairs: # O(V)
            if pair[0] == v: # O(1)
                return True # O(1)
        return False # O(1)

    # O(V)
    def _get_index(self, v)-> int | None:
        for pair in self.pairs: # O(V)
            if pair[0] == v: # O(1)
                return pair[1] # O(1)

def tests_adjacency_matrix_graph():
    # Initialize the graph
    ag = adjacencyMatrixGraph(6)
    
    # Add vertices
    ag.add_vertex(7)
    ag.add_vertex(8)
    
    # Add edges
    ag.add_edge(1, 2)
    ag.add_edge(1, 3)
    ag.add_edge(1, 5)
    ag.add_edge(1, 4)
    ag.add_edge(4, 5)
    ag.add_edge(2, 3)
    ag.add_edge(2, 5)
    ag.add_edge(3, 4)
    ag.add_edge(3, 5)
    
    # Print the graph
    ag.print_graph()
    
    # Test the number of edges
    assert ag.num_edges() == 9, "Incorrect number of edges"
    
    # Test remove_edge
    ag.remove_edge(1, 3)
    ag.remove_edge(2, 5)
    ag.print_graph()
    assert ag.num_edges() == 7, "Incorrect number of edges after removing edges"
    
    # Test remove_vertex
    ag.remove_vertex(1)
    ag.remove_vertex(3)
    ag.print_graph()
    assert not ag.contains(1), "Vertex 1 still exists after removal"
    assert not ag.contains(3), "Vertex 3 still exists after removal"
    assert ag.num_edges() == 1, "Incorrect number of edges after removing vertices"
    
    # Test get_neighbors
    assert ag.get_neighbors(2) == [], "Incorrect neighbors for vertex 2"
    assert ag.get_neighbors(5) == [4], "Incorrect neighbors for vertex 5"
    assert ag.get_neighbors(7) == [], "Incorrect neighbors for vertex 7"
    
    # Test contains
    assert ag.contains(2), "Vertex 2 not found"
    assert not ag.contains(1), "Vertex 1 found after removal"
    
    # Test _get_index
    assert ag._get_index(2) == 0, "Incorrect index for vertex 2"

    # Test adding edges with non-existing vertices
    ag.add_edge(10, 11)
    assert ag.num_edges() == 2, "Incorrect number of edges after adding edges with non-existing vertices"
    ag.print_graph()

    ag.remove_edge(7,9)
    assert ag.num_edges() == 2, "Incorrect number of edges after removing edge where it was not"

    # Test removing edges with non-existing vertices
    ag.remove_edge(15, 16)
    assert ag.num_edges() == 2, "Incorrect number of edges after removing edges with non-existing vertices"
    
    # Test adding existing edge
    ag.add_edge(4, 5)
    assert ag.num_edges() == 2, "Incorrect number of edges after Adding existing edge"

    # Test removing non-existing vertices
    ag.remove_vertex(18)
    assert ag.num_edges() == 2, "Incorrect number of edges after removing non-existing vertices"

    # Test get_neighbors for non-existing vertex
    assert ag.get_neighbors(19) == [], "Incorrect neighbors for non-existing vertex"

    # Test _get_index for non-existing vertex
    assert ag._get_index(14) is None, "Incorrect index for non-existing vertex"

    print('All tests passed successfully')
tests_adjacency_matrix_graph()

