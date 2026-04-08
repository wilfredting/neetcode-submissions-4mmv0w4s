class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr = -1
        for i in range(len(arr) -1, -1, -1):
            tmp = arr[i]
            arr[i] = curr
            if tmp > curr:
                curr = max(curr, tmp)
        return arr