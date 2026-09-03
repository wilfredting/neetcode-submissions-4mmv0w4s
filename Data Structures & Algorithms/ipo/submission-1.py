import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit, min_req = [], []

        for i in range(len(profits)):
            p, c = profits[i], capital[i]
            if w >= c:
                heapq.heappush(max_profit, (-p, c))
            else:
                heapq.heappush(min_req, (c, p))

        max_profits = w

        for i in range(k):
            if not max_profit:
                break
            p, c = heapq.heappop(max_profit)
            max_profits += -p

            while min_req and min_req[0][0] <= max_profits:
                c, p = heapq.heappop(min_req)
                heapq.heappush(max_profit, (-p, c))

        return max_profits
