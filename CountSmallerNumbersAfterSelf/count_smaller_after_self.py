class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # this solution is basically the mergesort algorithm with index and count tracking
        # the mergesort is done on a list of tuples with the format (index, value, count),
        # where count is the number of smaller elements after the current element (in the
        # original list)
        # so before starting the mergesort, the tuple-array is created
        nums = [[i, x, 0] for i,x in enumerate(nums)]
        tpls = self.mergesort(nums)
        ret = [0] * len(nums)
        for x in tpls:
            ret[x[0]] = x[2]
        return ret
    
    def mergesort(self, arr: List[List[int]]) -> List[List[int]]:
        if len(arr) == 1:
            return arr
        middle = len(arr) // 2
        return self.merge(self.mergesort(arr[:middle]), self.mergesort(arr[middle:]))
    
    def merge(self, left: List[List[int]], right: List[List[int]]) ->  List[List[int]]:
        # exactly the merge sort algorithm, but a tally is kept on the number of smaller
        # elements to the right of each left element (in the res array)
        l, r = 0, 0
        res = []
        count = 0
        while l < len(left) and r < len(right):
            if left[l][1] <= right[r][1]:
                res.append([left[l][0], left[l][1], left[l][2]+count])
                l += 1
            elif left[l][1] > right[r][1]:
                res.append(right[r])
                count += 1
                r += 1
        while l < len(left):
            res.append((left[l][0], left[l][1], left[l][2] + count))
            l += 1
        res.extend(right[r:])
        return res
