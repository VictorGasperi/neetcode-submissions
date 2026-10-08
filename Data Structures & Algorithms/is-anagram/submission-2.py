from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_freq_map = defaultdict(int)

        for char in s:
            s_freq_map[char] += 1

        for char in t:
            s_freq_map[char] -= 1
            if s_freq_map[char] < 0:
                return False

        return True