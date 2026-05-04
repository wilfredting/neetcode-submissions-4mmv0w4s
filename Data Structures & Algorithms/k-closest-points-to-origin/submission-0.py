import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return math.sqrt(pow(x, 2) + pow(y, 2))

        heap = [(distance(x, y), (x, y)) for x, y in points]
        heapq.heapify(heap)
        
        res = [heapq.heappop(heap)[1] for i in range(k)]

        return res