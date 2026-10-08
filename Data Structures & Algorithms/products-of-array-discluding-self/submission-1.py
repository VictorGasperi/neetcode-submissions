class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_mult = [1] * len(nums)
        sufix_mult = [1] * len(nums)
        res = []


        for i in range(1, len(nums)):

            prefix_mult[i] = prefix_mult[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):

            sufix_mult[i] = sufix_mult[i + 1] * nums[i + 1]

        for i in range(len(nums)):

            res.append(prefix_mult[i] * sufix_mult[i])

        return res

        