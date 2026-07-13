class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        num_set = set()

        for index, n in enumerate(nums):
            if n in num_set:
                return True
            num_set.add(n)
            if len(num_set) > k:
                num_set.remove(nums[index - k])

        return False                