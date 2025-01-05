class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = [0, 0]
        for i, x in enumerate(nums):
            ret[0] = i
            for i2, x2 in enumerate(nums):
                if i != i2:
                    if x + x2 == target:
                        ret[1] = i2
                        return ret
