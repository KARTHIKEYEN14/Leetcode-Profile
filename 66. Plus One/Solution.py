class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        for i in digits:
            res = res*10 + i 
        res += 1
        digits = list(map(int,str(res)))
        return digits