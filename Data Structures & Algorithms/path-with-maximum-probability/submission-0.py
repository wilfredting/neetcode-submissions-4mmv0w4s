import heapq
from collections import defaultdict


class Solution:
    def maxProbability(
        self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int
    ) -> float:
        adjList = defaultdict(list)
        for i, nodes in enumerate(edges):
            n1, n2 = nodes
            adjList[n1].append([n2, succProb[i]])
            adjList[n2].append([n1, succProb[i]])

        maximum = defaultdict(int)
        maxHeap = [(-1.0, start_node)]
        while maxHeap:
            succ, source = heapq.heappop(maxHeap)
            if source in maximum:
                continue
            maximum[source] = -succ

            for target, new_succ in adjList[source]:
                if target not in maximum:
                    heapq.heappush(maxHeap, (-(new_succ * -succ), target))

        return maximum[end_node]