class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        res = [x for x in s.split(" ")]
        return len(res[-1])