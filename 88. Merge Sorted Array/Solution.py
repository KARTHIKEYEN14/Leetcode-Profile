class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            nums1
        if m == 0 :
            nums1[:]= nums2
        for i in range(len(nums2)):
            if 0 in nums1:
                nums1.insert(nums1.index(0),nums2[i])
                nums1.remove(0)
        nums1.sort()