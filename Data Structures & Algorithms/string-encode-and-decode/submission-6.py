class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""

        for s in strs:
            encode += f"{len(s)}#{s}"

        return encode

    def decode(self, s: str) -> List[str]:
        ans = []

        i = 0
        while i < len(s):
            num_index = i
            while s[num_index].isnumeric():
                num_index += 1
            word_length = int(s[i:num_index])
            i = num_index + 1 + word_length
            ans.append(s[i - word_length:i])

        return ans
