from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        counts = Counter(nums)

        def recursive(arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return

            for num in list(counts):
                if not counts[num]:
                    continue

                counts[num] -= 1
                arr.append(num)
                recursive(arr)
                arr.pop()
                counts[num] += 1


        recursive([])
        return res