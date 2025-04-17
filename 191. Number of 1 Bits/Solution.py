class Solution(object):
    def hammingWeight(self, n):
        s = str(bin(n))
        return s.count("1")