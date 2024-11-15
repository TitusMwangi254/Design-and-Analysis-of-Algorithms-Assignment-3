class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.edges = []           # List to store edges

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])  # Path compression
        return parent[i]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        # Attach smaller rank tree under root of higher rank tree
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        # Sort edges by weight
        self.edges.sort()
        parent = list(range(self.vertices))
        rank = [0] * self.vertices
        mst = []

        for weight, u, v in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:
                mst.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)

        return mst


# Example usage
g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 4)
g.add_edge(3, 4, 2)
g.add_edge(4, 5, 6)

mst = g.kruskal_mst()
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v}, weight: {weight}")
