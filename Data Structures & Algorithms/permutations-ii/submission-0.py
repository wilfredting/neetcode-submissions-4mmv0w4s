class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def recursive(arr, numbers):
            if len(numbers) == 0:
                res.add(tuple(arr))

            for i, n in enumerate(numbers):
                copy = numbers.copy()
                copy.pop(i)
                arr.append(n)
                recursive(arr, copy)
                arr.pop()

        recursive([], nums)

        arrayRes = []
        for s in res:
            arrayRes.append(list(s))

        return arrayRes