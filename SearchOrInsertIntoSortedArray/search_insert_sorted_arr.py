class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search problem
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                return middle
        return left
