class Solution:
    def findMin(self, nums: List[int]) -> int:
        # modified binary search
        # target = right here
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left + right) // 2
            if nums[right] > nums[middle]:
                right = middle      # notice how this is used instead of middle - 1
            elif nums[right] < nums[middle]:
                left = middle + 1
            else:
                right -= 1      # instead of returning directly, prune the right by 1,
        return nums[middle]     # this somehow takes care of duplicates
