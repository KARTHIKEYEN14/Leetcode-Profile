class Solution(object):
    def singleNumber(self, nums):
        s = list(set(nums))
        for i in s:
            if nums.count(i) != 3:
                return i