1class Solution(object):
2    def maximum69Number (self, num):
3        num = list(str(num))
4        for i in range(len(num)):
5            if "6" == num[i]:
6                num[i] = "9"
7                break
8        return int(''.join(num))
9        