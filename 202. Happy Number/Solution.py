class Solution:
    def isHappy(self, n: int) -> bool:
        res = 0
        n = str(n)
        while(len(n)>1):
            for i in range(len(n)):
                res = res + ((int(n[i]))**2)
            n = str(res)
            res = 0
        if n == "1"or n == '7':
            return True
        return False