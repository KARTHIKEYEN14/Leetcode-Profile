class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i  in range(0,len(nums)):
                if(nums[i] == target):
                    return i
        else:
            for i in range(0,len(nums)):
                if nums[i]<target and nums[(i+1)%len(nums)]>target:
                    return i+1
                elif nums[i]>target:
                    return i 
                elif nums[len(nums)-1]<target:
                    nums.append(target)
                    return nums.index(target)
                else:
                    continue