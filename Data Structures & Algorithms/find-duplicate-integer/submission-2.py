class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                slow2 = 0

                while slow != slow2:
                    slow2 = nums[slow2]
                    slow = nums[slow]


                return slow