class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            numRes = len(res)
            for i in range(numRes):
                result = res[i]
                new = result.copy()
                new.append(num)
                res.append(new)
        
        return res