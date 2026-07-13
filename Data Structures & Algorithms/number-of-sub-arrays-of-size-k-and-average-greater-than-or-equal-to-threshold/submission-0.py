class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        totalSum = 0
        interval = 0

        for index, n in enumerate(arr):
            totalSum += n
            interval += 1

            if interval > k:
                interval -= 1
                totalSum -= arr[index - k]
            
            if interval == k:
                avg = totalSum / interval
                if avg >= threshold:
                    res += 1


        return res