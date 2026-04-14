class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mm = 0
        nn = 0
        end_m = m
        
        while mm < end_m and nn < n:
            if nums2[nn] < nums1[mm]:
                for i in range(end_m - mm):
                    nums1[end_m - i] = nums1[end_m - i - 1]
                nums1[mm] = nums2[nn]
                nn += 1
                end_m += 1
            mm += 1
        
        while nn < n:
            nums1[mm] = nums2[nn]
            mm += 1
            nn += 1