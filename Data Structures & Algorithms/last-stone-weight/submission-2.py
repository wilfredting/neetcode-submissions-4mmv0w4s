import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        data = [-x for x in stones]
        heapq.heapify(data)
        while len(data) > 1:
            x, y = -heapq.heappop(data), -heapq.heappop(data)
            if x > y:
                heapq.heappush(data, y - x)
        return -heapq.heappop(data) if len(data) == 1 else 0