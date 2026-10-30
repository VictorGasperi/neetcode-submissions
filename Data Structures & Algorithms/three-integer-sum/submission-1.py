class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        complementary = {}
        memory = set()
        res = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[j] in complementary:

                    for c_left, c_right in complementary[nums[j]][::-1]:

                        if j == c_left:
                            continue

                        if j == c_right:
                            continue

                        triple = sorted([nums[c_left], nums[c_right], nums[j]])

                        memory.add(tuple(triple))

                        complementary[nums[j]].remove((c_left, c_right))

                if (0 - (nums[i] + nums[j])) not in complementary:
                    complementary[(0 - (nums[i] + nums[j]))] = []

                complementary[(0 - (nums[i] + nums[j]))].append((i ,j))

        return [[x[0], x[1], x[2]] for x in memory]

