import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums.copy() + [-1001]
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        heapq.heappop(self.heap)
        return self.heap[0]
        
