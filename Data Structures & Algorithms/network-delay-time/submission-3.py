from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for source, target, time in times:
            adjList[source].append([target, time])

        shortest = {}
        minHeap = [(0, k)]
        while minHeap:
            time, source = heapq.heappop(minHeap)
            if source in shortest:
                continue
            shortest[source] = time

            for target, newTime in adjList[source]:
                if target not in shortest:
                    heapq.heappush(minHeap, (time + newTime, target))

        res = -1
        for i in range(1, n + 1):
            if i not in shortest:
                return - 1
            res = max(res, shortest[i])

        return res
