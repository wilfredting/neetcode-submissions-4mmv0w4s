class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digitToLetters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(i, curr, res):
            if len(curr) == len(digits):
                res.append(curr)
                return

            for char in digitToLetters[digits[i]]:
                curr += char
                dfs(i + 1, curr, res)
                curr = curr[0:-1]


        res = []
        dfs(0, "", res)
        return res
