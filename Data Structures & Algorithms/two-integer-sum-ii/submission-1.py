class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R:
            s = numbers[L] + numbers[R]
            if s == target:
                return [L + 1, R + 1]
            elif s < target:
                L += 1
            else:
                R -= 1