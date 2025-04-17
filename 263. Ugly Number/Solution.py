class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        l = [2,3,5]
        i = 0
        res = 0
        while(i<len(l)-2):
            if n%l[i] == 0:
                res = int(n/l[i])
                n = res
            elif n%l[i+1] ==0:
                res = int(n/l[i+1])
                n = res
            elif n%l[i+2] == 0:
                res = int(n/l[i+2])
                n = res
            else:
                i += 1
        if res == 1:
            return True
        return False