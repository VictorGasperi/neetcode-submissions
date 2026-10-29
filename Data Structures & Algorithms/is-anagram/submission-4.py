class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq = {}

        for s_char, t_char in zip(s, t):

            if s_char not in freq:
                freq[s_char] = 0

            freq[s_char] += 1

            if t_char not in freq:
                freq[t_char] = 0

            freq[t_char] -= 1

        return all([x == 0 for x in freq.values()])