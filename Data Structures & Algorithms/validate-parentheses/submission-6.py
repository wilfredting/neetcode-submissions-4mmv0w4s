class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {')':'(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c in parentheses_map:
                if not stack or stack[-1] != parentheses_map[c]:
                    return False
                stack.pop(-1);
            else:
                stack.append(c);
        return len(stack) == 0
