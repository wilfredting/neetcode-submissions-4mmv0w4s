class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 1

    def find(self, n):
        while n != self.parent[n]:
            self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]
        return n

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        union = UnionFind(n)

        for [x,y] in edges:
            if not union.union(x,y):
                return [x,y]
