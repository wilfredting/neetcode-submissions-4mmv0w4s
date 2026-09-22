from collections import Counter

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)
        def recursive(arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return

            for n in list(count):
                if not count[n]:
                    continue

                count[n] -= 1
                arr.append(n)
                recursive(arr)
                arr.pop()
                count[n] += 1
                
        recursive([])
        return res