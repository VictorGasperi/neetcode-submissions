from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = defaultdict(int)
        freq_bucket = [[] * x for x in range(len(nums) + 1)]
        res = []

        for num in nums:
            freq_map[num] += 1

        for num, freq in freq_map.items():
            freq_bucket[freq].append(num)

        for i in range(len(freq_bucket) - 1, 0, -1):
            for j in range(len(freq_bucket[i])):

                res.append(freq_bucket[i][j])

                if len(res) == k:
                    return res