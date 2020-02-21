graph = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2},
         'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}


def dijkstra(graph: dict, start: str, goal: str):
    """Connect to all nodes to calculate the shortest route"""
    shortest_distance = {}
    predecessor = {}
    unseen_nodes = graph
    infinity = float('inf')
    path = []

    # Set all unseen nodes to infinity
    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            # Calculate which remaining node is closest to node
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for child_node, weight in graph[min_node].items():
            # Calculate the shortest route and store the path
            if shortest_distance[min_node] + weight < shortest_distance[child_node]:
                shortest_distance[child_node] = shortest_distance[min_node] + weight
                predecessor[child_node] = min_node
        unseen_nodes.pop(min_node)

    # Run through path backwards
    current_node = goal
    while current_node != start:
        path.insert(0, current_node)
        current_node = predecessor[current_node]
    path.insert(0, start)

    print(f"Shortest path from {start} to {goal} is {str(shortest_distance[goal])}")
    print(f"The path is {path}")


if __name__ == '__main__':
    dijkstra(graph.copy(), 'a', 'd')
    dijkstra(graph.copy(), 'a', 'e')
    dijkstra(graph.copy(), 'c', 'd')
