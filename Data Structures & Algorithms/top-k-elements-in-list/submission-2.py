class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:

            if num not in freq_map:
                freq_map[num] = 0

            freq_map[num] += 1

        for num, freq in freq_map.items():

            bucket[freq].append(num)

        for i in range(len(bucket) - 1, -1, -1):
            for j in range(len(bucket[i])):

                res.append(bucket[i][j])

                if len(res) == k:
                    break

            if len(res) == k:
                    break

        return res