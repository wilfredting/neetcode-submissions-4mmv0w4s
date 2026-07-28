class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L = 0
        res = 1
        sign = None

        for R in range(1, len(arr), 1):
            curr_sign = (arr[R] > arr[R-1]) - (arr[R] < arr[R-1])
           
            if curr_sign == 0:
                L = R
                sign = None
                continue

            if sign is not None and curr_sign != -sign:
                L = R - 1


            sign = curr_sign
            res = max(res, R - L + 1)

        return res