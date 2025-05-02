class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge sort to combine sorted arrays
        left = 0
        right = 0
        m = len(nums1)
        n = len(nums2)
        merged = []
        while left < m and right < n:
            if nums1[left] > nums2[right]:
                merged.append(nums2[right])
                right += 1
            else:
                merged.append(nums1[left])
                left += 1
        merged.extend(nums1[left:])
        merged.extend(nums2[right:])
        # then just return the median
        if (m+n)%2 == 1:
            return merged[(m+n)//2]
        else:
            return (merged[(m+n)//2-1] + merged[(m+n)//2])/2
