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
maxi_limit = 4

def dls(node, limit):
    visited = set()
    print("Curr limit: ", limit)

    def dfs(node, limit):
        if limit == 0:
            return
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for i in tree[node]:
                dfs(i, limit-1)
    dfs(node, limit)
    print()
    print()


for i in range(1, maxi_limit+1):
    dls(1, i)
