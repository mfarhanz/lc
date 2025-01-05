class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = m - 1
        n2 = n - 1
        curr = m + n - 1
        if m == 0 and n != 0:
            nums1[:] = nums2
            return
        elif m == n == 0 or n == 0 and m != 0:
            return
        while n2 >= 0:
            if n1 >= 0 and nums1[n1] >= nums2[n2]:
                nums1[curr] = nums1[n1]
                n1 -= 1
            else:
                nums1[curr] = nums2[n2]
                n2 -= 1
            curr -= 1
