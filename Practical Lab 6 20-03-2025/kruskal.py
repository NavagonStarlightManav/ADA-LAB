class DSU:
    def __init__(self, n):
        self.parent = [-1] * n  # -1 means root and size is 1

    def find(self, u):
        if self.parent[u] < 0:
            return u
        self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU == rootV:
            return False  # Already connected

        # Union by size
        if self.parent[rootU] < self.parent[rootV]:
            self.parent[rootU] += self.parent[rootV]
            self.parent[rootV] = rootU
        else:
            self.parent[rootV] += self.parent[rootU]
            self.parent[rootU] = rootV

        return True


def kruskalMST(n, edges):
    # Sort edges by weight
    edges.sort()

    dsu = DSU(n)
    min_cost = 0
    edges_used = 0

    for w, u, v in edges:
        if dsu.union(u, v):
            min_cost += w
            edges_used += 1
            print(f"Edge: ({u} - {v}) with cost: {w}")

        if edges_used == n - 1:
            break

    if edges_used == n - 1:
        print(f"Minimum Spanning Tree Cost: {min_cost}")
    else:
        print("MST not possible!")


# 🔸 Sample Usage
n = 4  # Number of vertices
edges = [
    (10, 0, 1),
    (6, 0, 2),
    (5, 1, 2),
    (15, 1, 3),
    (4, 2, 3)
]

kruskalMST(n, edges)
