class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digitToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, curr, res):
            if len(curr) == len(digits):
                res.append(curr)
                return

            for char in digitToLetters[digits[i]]:
                dfs(i + 1, curr + char, res)

        res = []
        dfs(0, "", res)
        return res
