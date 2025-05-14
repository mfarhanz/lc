class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # exactly the mergesort algorithm, but made neater by compressing into one
        # function, and without using any built-in funtions
        # to have the lowest space complexity, instead of making a new array everytime,
        # the same original array is modified inplace, everytime function recurses
        n = 0
        for x in nums:
            n += 1
        if n > 1:
            left = nums[:n//2]
            right = nums[n//2:]
            self.sortArray(left)
            self.sortArray(right)
            l, r, i = 0, 0, 0
            ln = n // 2
            rn = n // 2 if n % 2 == 0 else n // 2 + 1
            while l < ln and r < rn:
                if left[l] < right[r]:
                    nums[i] = left[l]
                    l += 1
                else:
                    nums[i] = right[r]
                    r += 1
                i += 1
            for x in left[l:] + right[r:]:
                nums[i] = x
                i += 1
        return nums
