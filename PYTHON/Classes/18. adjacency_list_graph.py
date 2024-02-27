class Adjacency_list_graph:
    # Time: O(1)
    def __init__(self) -> None:
        self.graph = {}

    # Time: O(V + E)
    def print_graph(self) -> None:
        for vertex in self.graph:
            print(f"'{vertex}': {self.graph[vertex]}")

    # Time: O(1)
    def add_vertex(self, vertex) -> None:
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Time: O(min(V, E))
    def add_edge(self, vertex1, vertex2) -> None:
        if vertex1 not in self.graph: # O(1)
            self.add_vertex(vertex1)  # O(1)
        if vertex2 not in self.graph: # O(1)
            self.add_vertex(vertex2)  # O(1)

        if vertex2 not in self.graph[vertex1]:   # O(min(V, E))
            self.graph[vertex1].append(vertex2)  # O(1)
            self.graph[vertex2].append(vertex1)  # O(1)

    # Time: O(min(V, E))
    def remove_edge(self, vertex1, vertex2) -> None:
        self.graph[vertex1].remove(vertex2) # O(min(V, E))
        self.graph[vertex2].remove(vertex1) # O(min(V, E))

    # Time: O(min(V, E) * min(V, E))
    def remove_vertex(self, vertex) -> None:
        for other_vertex in self.graph[vertex]: # O(min(V, E))
            self.graph[other_vertex].remove(vertex) # # O(min(V, E))
        self.graph.pop(vertex) # O(1)

def tests_adjacency_list():
    # Initialize the graph
    adj_list = Adjacency_list_graph()

    # Add vertices
    adj_list.add_vertex('A')
    adj_list.add_vertex('B')
    adj_list.add_vertex('C')
    adj_list.add_vertex('D')

    # Add edges
    adj_list.add_edge('A', 'B')
    adj_list.add_edge('A', 'C')
    adj_list.add_edge('B', 'D')
    adj_list.add_edge('C', 'D')

    # Print the graph
    print("Graph after adding vertices and edges:")
    adj_list.print_graph()

    # Test remove_edge
    adj_list.remove_edge('A', 'C')
    print("\nGraph after removing edge ('A', 'C'):")
    adj_list.print_graph()
    assert 'C' not in adj_list.graph['A'], "Edge ('A', 'C') not removed from 'A' adjacency list"
    assert 'A' not in adj_list.graph['C'], "Edge ('A', 'C') not removed from 'C' adjacency list"

    # Test remove_vertex
    adj_list.remove_vertex('B')
    print("\nGraph after removing vertex 'B':")
    adj_list.print_graph()
    assert 'B' not in adj_list.graph, "Vertex 'B' not removed from the graph"
    assert 'D' not in adj_list.graph['A'], "Edge ('A', 'B') not removed from 'A' adjacency list"
    assert 'A' not in adj_list.graph['D'], "Edge ('A', 'B') not removed from 'D' adjacency list"

    # Test add_edge with non-existing vertices
    adj_list.add_edge('E', 'F')
    print("\nGraph after adding edge ('E', 'F') with non-existing vertices:")
    adj_list.print_graph()
    assert 'E' in adj_list.graph, "Vertex 'E' not added to the graph"
    assert 'F' in adj_list.graph, "Vertex 'F' not added to the graph"
    assert 'E' in adj_list.graph['F'], "Edge ('E', 'F') not added to 'F' adjacency list"
    assert 'F' in adj_list.graph['E'], "Edge ('E', 'F') not added to 'E' adjacency list"

    # Test add_vertex with existing vertex
    adj_list.add_vertex('A')
    print("\nGraph after adding existing vertex 'A':")
    adj_list.print_graph()

    # Test remove_vertex with existing vertex
    adj_list.remove_vertex('A')
    print("\nGraph after removing existing vertex 'A':")
    adj_list.print_graph()
    assert 'A' not in adj_list.graph, "Vertex 'A' not removed from the graph"

    print('All tests passed successfully')

# Run the tests
tests_adjacency_list()
