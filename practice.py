Graph = {
    "A": ["B", "C", "D"],
    "B": ["E", "C", "A"],
    "C": ["A", "E", "H", "G", "F"],
    "D": ["A", "H"],
    "E": ["B", "C", "F"],
    "F": ["E", "C", "I"],
    "G": ["C", "H", "I"],
    "H": ["C", "D", "G"],
    "I": ["F", "G"],

}


def BFS(Graph, root):
    queue = []
    queue.append(root)

    visited = set()
    visited.add(root)

    while len(queue) > 0:
        vertex = queue.pop(0)
        neighbors = Graph[vertex]
        for node in neighbors:
            if node not in visited:
                queue.append(node)
                visited.add(node)
        print(vertex)


BFS(Graph, "A")
print("\n")


def DFS(Graph, root):
    stack = []
    stack.append(root)

    visited = set()
    visited.add(root)

    while len(stack) > 0:
        vertex = stack.pop()
        neighbors = Graph[vertex]
        for node in neighbors:
            if node not in visited:
                stack.append(node)
                visited.add(node)
        print(vertex)


DFS(Graph, "A")