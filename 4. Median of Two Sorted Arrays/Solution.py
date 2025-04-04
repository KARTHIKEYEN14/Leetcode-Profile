class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
        res = nums1 + nums2
        res.sort()
        l = len(res)
        mid = int(l/2)
        if(l%2 == 0):
            return (res[mid]+res[mid-1])/2
        else:
            return res[mid]

        