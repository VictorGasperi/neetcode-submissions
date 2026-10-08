class Solution:

    def encode(self, strs: List[str]) -> str:

        for i in range(len(strs)):

            size = len(strs[i])
            strs[i] = f'{size}#' + strs[i]

        print(''.join(strs))

        return ''.join(strs)

    def decode(self, s: str) -> List[str]:
        
        res = []
        left = right = 0

        while left < len(s):

            aux = []

            while s[right] != '#':

                right += 1

            size = int(s[left:right])

            left = right + 1
            right = size + left

            aux = s[left:right]

            res.append(aux)
            left = right

        return res