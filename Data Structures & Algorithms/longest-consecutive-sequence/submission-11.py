class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.longest = 0

    def add(self, n):
        if n in self.parent:
            return
        self.parent[n] = n
        self.rank[n] = 1
        self.longest = max(self.longest, 1)

    def find(self, n):
        while n != self.parent[n]:
            self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]
        return n

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False

        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
            self.longest = max(self.longest, self.rank[pa])
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]
            self.longest = max(self.longest, self.rank[pb])
        
        return True
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind()

        for num in nums:
            uf.add(num)
            if num - 1 in uf.parent:
                uf.union(num - 1, num)
            if num + 1 in uf.parent:
                uf.union(num + 1, num)
            
        return uf.longest

        # num_set = set(nums)
        # res = 0

        # for num in nums:
        #     if num - 1 not in num_set:
        #         length = 1
        #         while num + length in num_set:
        #             length += 1
        #         res = max(res, length)

        # return res

        