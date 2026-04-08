class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = 0
        for num in nums:
            if num != val:
                nums[answer] = num
                answer += 1
        return answer
        