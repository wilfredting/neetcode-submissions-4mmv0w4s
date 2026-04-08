class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if len(stack) > 0:
                    removed = stack.pop()
                    if c == ')' and removed != '(':
                        return False
                    if c == '}' and removed != '{':
                        return False
                    if c == ']' and removed != '[':
                        return False
                else:
                    return False
        return len(stack) == 0