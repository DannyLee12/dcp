"""DFS uses less memory, can be faster for deep and not wide graphs"""
graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}


def dfs(graph, node, visited=None):
    if visited is None:
        visited = []

    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)

    return visited


if __name__ == '__main__':
    print(dfs(graph1, 'A'))
