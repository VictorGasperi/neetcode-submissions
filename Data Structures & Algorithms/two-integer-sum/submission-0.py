from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement_map = defaultdict(int)

        for idx, num in enumerate(nums):

            if num in complement_map:
                return [complement_map[num], idx]

            complement_map[target - num] = idx

        