class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for x in range(len(points)):
            for y in range(x + 1, len(points)):
                p1, p2 = points[x], points[y]
                dist = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
                edges.append([dist, x, y])
        
        edges.sort()
        unionFind = UnionFind(len(points))
        res = 0
        count = 0

        for i in range(len(edges)):
            dist, n1, n2 = edges[i]
            if not unionFind.union(n1, n2):
                continue
            count += 1
            res += dist
            if count == len(points) - 1:
                break
        return res