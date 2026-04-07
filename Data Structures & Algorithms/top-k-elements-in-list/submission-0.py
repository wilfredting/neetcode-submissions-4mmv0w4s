class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = [[] for _ in range(len(nums) + 1)]
        count_map = defaultdict(int)

        for num in nums:
            count_map[num] += 1

        for key, value in count_map.items():
            num_count[value].append(key)

        print(num_count)
        ans = []
        for i in range(len(num_count) - 1, -1 ,-1):
            ans.extend(num_count[i])
            if len(ans) >= k:
                return ans

        return ans