tree = {
    1: [2, 4],
    2: [3],
    4: [5],
    3: [],
    5: []
}

visited = set()
queue = []

print("BFS: ")


def bfs(node):
    visited.add(node)
    queue.append(node)
    while queue:
        n = queue.pop(0)
        print(n, end=" ")
        for i in tree[n]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

bfs(1)
