class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        pos = [-1, -1]
        # binary search
        while left <= right:
            middle = (left + right) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                # forward and backward pointer strat
                lower = middle
                upper = middle
                moved = True
                while moved:
                    moved = False
                    if lower-1 >= 0 and nums[lower-1] == target:
                        lower -= 1
                        moved = True
                    if upper+1 < n and nums[upper+1] == target:
                        upper += 1
                        moved = True
                if lower >= 0:
                    pos[0] = lower
                if upper < n:
                    pos[1] = upper
                break
        return pos
