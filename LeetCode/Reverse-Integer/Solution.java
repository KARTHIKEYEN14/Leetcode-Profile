1class Solution:
2    def reverse(self, x: int) -> int:
3        if(x<0):
4            temp = -(x)
5            reverse = 0 
6            while(temp!=0):
7                rem = temp%10
8                reverse = reverse*10 + rem
9                temp //= 10
10            reverse = -(reverse)
11        else:
12            temp = x
13            reverse = 0 
14            while(temp!=0):
15                rem = temp%10
16                reverse = reverse*10 + rem
17                temp //= 10
18        result = reverse if ((-2**31)< reverse < ((2**31)-1)) else 0
19        return result