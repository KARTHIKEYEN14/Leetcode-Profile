class Solution:
    def reverse(self, x: int) -> int:
        if(x<0):
            temp = -(x)
            reverse = 0 
            while(temp!=0):
                rem = temp%10
                reverse = reverse*10 + rem
                temp //= 10
            reverse = -(reverse)
        else:
            temp = x
            reverse = 0 
            while(temp!=0):
                rem = temp%10
                reverse = reverse*10 + rem
                temp //= 10
        result = reverse if ((-2**31)< reverse < ((2**31)-1)) else 0
        return result