"""Explanation

Union-Find Data Structure: Helps in managing disjoint sets and checking if two vertices belong to the same set.
Sorting Edges: Edges are sorted by their weight in ascending order.
Building the MST: Edges are added to the MST if they don't form a cycle, which is checked using the Union-Find data structure.


"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1

def kruskal(n, edges):
    # Number of vertices is n, edges is a list of (weight, u, v)
    uf = UnionFind(n)
    mst = []
    
    # Sort edges based on weight
    edges.sort(key=lambda x: x[0])
    
    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
    
    return mst

# Example usage:
n = 4  # Number of vertices
edges = [
    (10, 0, 1),
    (6, 0, 2),
    (5, 1, 2),
    (15, 1, 3),
    (4, 2, 3)
]

mst = kruskal(n, edges)
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")
