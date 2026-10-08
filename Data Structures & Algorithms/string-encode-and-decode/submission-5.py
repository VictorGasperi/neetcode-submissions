class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []
        for word in strs:
            res.append(f"{len(word)}#{word}")

        return ''.join(res)

    def decode(self, s: str) -> List[str]:

        print(s)

        left = right = 0
        res = []

        while left < len(s):

            while s[right] != '#':
                right += 1

            aux = s[left:right]
            left = right + 1
            right = right + int(aux) + 1

            res.append(s[left:right])
            left = right

        return res