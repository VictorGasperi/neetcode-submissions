class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        seq_starts = []
        res = 0

        for num in nums_set:

            if num - 1 not in nums_set:
                seq_starts.append(num)

        for num in seq_starts:

            curr = num
            aux = 1

            while curr + 1 in nums_set:
                aux += 1
                curr += 1

            res = max(res, aux)

        return res
                