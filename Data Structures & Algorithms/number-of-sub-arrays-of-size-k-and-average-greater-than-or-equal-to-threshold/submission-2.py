class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        target = k * threshold
        totalSum = sum(arr[:k - 1])

        for index in range(k - 1, len(arr)): 
            totalSum += arr[index]
            if totalSum >= target:
                res += 1
            totalSum -= arr[index - (k - 1)]

        return res