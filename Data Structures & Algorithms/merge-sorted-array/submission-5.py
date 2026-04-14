class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mm = m - 1
        nn = n - 1
        curr = len(nums1) - 1

        while nn >= 0:
            if mm >= 0 and nums1[mm] > nums2[nn]:
                nums1[curr] = nums1[mm]
                mm -= 1
            else:
                nums1[curr] = nums2[nn]
                nn -=1
            curr -= 1
