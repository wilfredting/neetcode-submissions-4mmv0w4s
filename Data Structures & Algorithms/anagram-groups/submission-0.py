class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            str_map[sorted_str].append(s)

        return str_map.values()