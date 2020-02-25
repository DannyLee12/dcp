graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B', 'E'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}

g2 = {"1": ["2", "3"],
      "2": ["1"],
      "3": ["1", "0", "4", "6"],
      "4": ["5", "3"],
      "5": ["0", "4"],
      "6": ["3"],
      "7": ["8"],
      "8": ["7"],
      "0": ["5", "3"]}


def bfs_shortest_path(graph: dict=g2, start: str = "1", goal: str = "4") -> list:
    """BFS shortest path, test conditions"""
    visited = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = path[:]
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            visited.append(node)
    # No path
    return ["No Path"]


def bfs(graph, initial):
    visited = []

    queue = [initial]

    while queue:
        node = queue.pop(0)
        if node not in visited:

            visited.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)
    return visited


if __name__ == '__main__':
    print(bfs_shortest_path(g2, "1", "7"))
