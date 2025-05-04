class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        k = None
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                k = i+1
                break
        check = target <= nums[k:][-1]
        if check:
            arr = nums[k:]
        else:
            arr = nums[:k]
        left = 0
        right = len(arr) - 1
        while left <= right:
            middle = (left + right)//2
            if target < arr[middle]:
                right = middle - 1
            elif target > arr[middle]:
                left = middle + 1
            else:
                return middle + k if check and k is not None else middle
        return -1
        
