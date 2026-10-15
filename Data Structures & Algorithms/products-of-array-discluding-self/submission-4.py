class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mult = [1] * len(nums)
        sufix_mult = [1] * len(nums)

        for i in range(1, len(nums)):

            curr = prefix_mult[i - 1] * nums[i - 1]
            prefix_mult[i] = curr

        for i in range(len(nums) - 2, -1, -1):

            curr = sufix_mult[i + 1] * nums[i + 1]
            sufix_mult[i] = curr

        return [i * j for i, j in zip(prefix_mult, sufix_mult)]