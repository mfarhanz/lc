class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        lookup = {}
        for i in nums:
            lookup[i] = target - i
        choices = list(lookup.items())
        for (i, j) in choices:
            if i == j:
                dup_indexes = [x for x, y in enumerate(nums) if y == j]
                if len(dup_indexes) > 1:
                    return [nums.index(i), dup_indexes[1]]
            else:
                if (j, i) in choices:
                    return [nums.index(i), nums.index(j)]
