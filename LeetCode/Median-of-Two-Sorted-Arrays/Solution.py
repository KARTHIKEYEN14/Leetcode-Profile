1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        res = nums1 + nums2
4        res.sort()
5        l = len(res)
6        mid = int(l/2)
7        if(l%2 == 0):
8            return (res[mid]+res[mid-1])/2
9        else:
10            return res[mid]