class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [1] * n

        def findParent(a):
            curr = a
            while parents[curr] != curr:
                parents[curr] = parents[parents[curr]]
                curr = parents[curr]
            return curr

        def union(a, b):
            parent_a = findParent(a)
            parent_b = findParent(b)

            if parent_a == parent_b:
                return 0
            elif ranks[parent_a] >= ranks[parent_b]:
                ranks[parent_a] += ranks[parent_b]
                parents[parent_b] = parent_a
                return 1
            else:
                ranks[parent_b] += ranks[parent_a]
                parents[parent_a] = parent_b
                return 1

        count = n
        for a, b in edges:
            count -= union(a, b)
        return count