class Solution:
    def isValid(self, s: str) -> bool:
        muh_list = []
        for p in s:
            if p in ['(', '{', '[']:
                muh_list.append(p)
            elif muh_list and muh_list[-1] == '(' and p == ')':
                muh_list.pop(-1)
            elif muh_list and muh_list[-1] == '[' and p == ']':
                muh_list.pop(-1)
            elif muh_list and muh_list[-1] == '{' and p == '}':
                muh_list.pop(-1)
            else:
                return False
        return not muh_list