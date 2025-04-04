class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend < 0 :
            dividend = -(dividend)
            res =  int(-(dividend / divisor))
        elif divisor < 0:
            divisor = - (divisor)
            res =  int(- (dividend /divisor) )
        else:
            res = int(dividend / divisor )
        if res > (2)**31 - 1:
            return (2)**31 -1
        elif res < -(2)**31:
            return -(2)**31
        else:
            return res
        