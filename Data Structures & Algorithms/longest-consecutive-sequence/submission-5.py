class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        startOfSeq = []
        res = 0

        for n in nums_set:

            if n - 1 not in nums_set:
                startOfSeq.append(n)

        for n in startOfSeq:

            curr = n
            maxSeq = 1
            
            while curr + 1 in nums_set:

                curr = curr + 1
                maxSeq += 1

            res = max(res, maxSeq)

        return res
    