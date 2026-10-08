class Solution:

    def encode(self, strs: List[str]) -> str:
        normalized = [""] + strs 
        return '#5'.join(normalized)

    def decode(self, s: str) -> List[str]:
        return s.split('#5')[1:]