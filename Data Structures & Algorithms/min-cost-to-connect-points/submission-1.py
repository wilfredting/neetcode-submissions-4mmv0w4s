import heapq
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for x in range(len(points)):
            for y in range(x + 1, len(points)):
                dist = abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
                adj[x].append([y, dist])
                adj[y].append([x, dist])

        minHeap = []
        for neighbor, weight in adj[0]:
            heapq.heappush(minHeap, [weight, neighbor])

        visit = set()
        visit.add(0)

        res = 0
        
        while len(visit) < len(points):
            weight, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue
            
            res += weight
            visit.add(n2)
            for neighbor, weight in adj[n2]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, neighbor])

        return res