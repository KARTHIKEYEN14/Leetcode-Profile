class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = nums[0]
        for i in range(0,len(nums)-1):
            nums[i] = a
            a = nums[i] ^ nums[i+1]
        return a