class Solution(object):
    def sortColors(self, nums):
        r = nums.count(0)
        w = nums.count(1)
        b = nums.count(2)
        a = [0]*r+[1]*w+[2]*b
        nums[:] = a