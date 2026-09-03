import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit, min_req = [], [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_req)

        for _ in range(k):
            while min_req and min_req[0][0] <= w:
                _, p = heapq.heappop(min_req)
                heapq.heappush(max_profit, -p)

            if not max_profit:
                break

            w += -heapq.heappop(max_profit)

        return w
