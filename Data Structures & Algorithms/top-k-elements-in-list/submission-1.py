from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}
        k_most_frequent = []

        for num in nums:

            if num not in freq_map:
                freq_map[num] = 0

            freq_map[num] += 1

        for num, freq in freq_map.items():
            
            if len(k_most_frequent) < k:
                heappush(k_most_frequent, (freq, num))
                continue
            
            if freq > k_most_frequent[0][0]:

                heappop(k_most_frequent)
                heappush(k_most_frequent, (freq, num))

        res = [x[1] for x in k_most_frequent]

        return res