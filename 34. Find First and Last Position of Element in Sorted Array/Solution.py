class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        res = []
        for i in range(len(nums)):
            if target == nums[i]:
                res.append(i)
                nums[i] = " "
                if target not in nums:
                    break
        return [res[0],res[-1]]
