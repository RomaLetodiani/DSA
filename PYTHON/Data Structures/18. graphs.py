# Adjacency list
# Space: O(V + E)
graph = {
    "A": ["E", "G", "B", "A"],
    "B": ["E", "D", "C"],
    "C": ["B", "D"],
    "D": ["B", "C", "E"],
    "E": ["A", "B", "D"],
    "G": ["A"]
}

# add_vertex -> O(1)
# add_edge -> O(1)
# remove_edge -> O(min(V, E))
# remove_vertex -> O(V * min(V, E)) => O(V^2) or O(V * E)

# --------------------------
# Adjacency matrix
# Space: O(V^2)
graph = [
    "A""B""C""D""E""G"
"A" [0, 0, 0, 0, 1, 1],
"B" [0, 0, 1, 1, 1, 0],
"C" [0, 1, 0, 1, 0, 0],
"D" [0, 1, 1, 0, 1, 0],
"E" [1, 1, 0, 1, 0, 0],
"G" [1, 0, 0, 0, 0, 0]
]

# add_vertex -> O(V)
# add_edge -> O(1)
# remove_edge -> O(1)
# remove_vertex -> O(V^2)


# -------------------------
# Nodes

class Node:
    def __init__(self, value) -> None:
        self.value = None
        self.neighbors = []

graph = [Node("A"), Node("B"), Node("C"), Node("D"), Node("E")]
graph[0].neighbors.append(graph[1])
