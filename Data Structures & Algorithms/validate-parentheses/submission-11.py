class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = { ')' : '(', '}' : '{', ']' : '[' }
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if stack and bracket_dict[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack