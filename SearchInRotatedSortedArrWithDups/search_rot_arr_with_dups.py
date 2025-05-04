class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # finding the pivot index
        k = 0
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                k = i + 1
                break
        # use only the side of array having target (doesnt matter if duplicates present)
        if target <= nums[k:][-1]:
            arr = nums[k:]
        else:
            arr = nums[:k]
        # binary search
        left = 0
        right = len(arr) - 1
        while left <= right:
            middle = (left + right) // 2
            if target < arr[middle]:
                right = middle - 1
            elif target > arr[middle]:
                left = middle + 1
            else:
                return True
        return False
