class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_visited = set()

        for num in nums:
            if num in has_visited:
                return True
            else:
                has_visited.add(num)

        return False