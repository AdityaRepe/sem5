tree = {
    1: [2, 3, 4, 5],
    2: [],
    3: [6, 7],
    4: [],
    5: [8, 9],
    6: [],
    7: [10],
    8: [11],
    9: [],
    10: [],
    11: []
}
visited = set()


def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for i in tree[node]:
            dfs(i)


dfs(1)
