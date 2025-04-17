class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        n = list(set(nums))
        for j,i in enumerate(n):
            if nums.count(i)>count:
                count = nums.count(i)
                maxi = n[j]
        return maxi