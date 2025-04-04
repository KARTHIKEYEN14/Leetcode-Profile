class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = nums.copy()
        nums.clear()
        count = 1
        i = 0 
        nums.append(res[0])
        while(i<len(res)-1 and res[i] <= res[i+1]):
            if res[i] == res[i+1]:
                i += 1
            else:
                nums.append(res[i+1])
                count += 1
                i += 1
        return count 

        
        
        