class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ''

        for s in strs:
            encode += f"{len(s)}#{s}"

        return encode

    def decode(self, s: str) -> List[str]:
        decode = []

        i = 0
        while i < len(s) - 1:
            hash_index = i + s[i:].find('#')
            length = int(s[i:hash_index])
            i = hash_index + 1 + length
            word = s[hash_index + 1 : i]
            decode.append(word)

        return decode
