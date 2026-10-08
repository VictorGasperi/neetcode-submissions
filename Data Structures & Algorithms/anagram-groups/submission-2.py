class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:

            group = [0] * 26

            for char in word:

                pos = ord(char) - ord('a')
                group[pos] += 1

            if tuple(group) not in groups:

                groups[tuple(group)] = []

            groups[tuple(group)].append(word)

        return list(groups.values())