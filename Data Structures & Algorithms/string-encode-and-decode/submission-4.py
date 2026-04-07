class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []

        for s in strs:
            ans.append(f"{len(s)}#{s}")

        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []

        i = 0
        while i < len(s):
            num_index = i
            while s[num_index].isnumeric():
                num_index += 1
            num_characters = int(s[i:num_index])
            i = num_index + 1 + num_characters
            ans.append(s[i-num_characters:i])

        return ans
