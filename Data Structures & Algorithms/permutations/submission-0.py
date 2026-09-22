class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recursive(arr, numbers):
            if len(numbers) == 0:
                res.append(arr.copy())

            for i, n in enumerate(numbers):
                copyNums = numbers.copy()
                copyNums.pop(i)
                arr.append(n)
                recursive(arr, copyNums)
                arr.pop()

        recursive([], nums)
        return res