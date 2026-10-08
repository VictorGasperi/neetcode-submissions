class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0
        set_nums = set(nums)
        start_of_seq = []

        for num in set_nums:

            if num - 1 not in set_nums:

                start_of_seq.append(num)

        for start_num in start_of_seq:

            curr_seq = 1
            prev = start_num
            while prev + 1 in set_nums:
                curr_seq += 1
                prev += 1

            res = max(res, curr_seq)

        return res
                