class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        elif nums[1] < nums[0]:
            return 0
        elif nums[n - 2] < nums[n - 1]:
            return n - 1
        # uses binary search's divide and conquer technique
        left = 0
        right = n - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < nums[middle-1] or nums[middle] < nums[middle+1]:
                if nums[middle-1] > nums[middle+1]:
                    right = middle
                else:
                    left = middle
            else:
                break
        return middle
      
