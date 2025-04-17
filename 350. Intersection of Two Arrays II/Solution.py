class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        res = []
        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j]:
                    res.append(nums2[j])
                    break
        return res