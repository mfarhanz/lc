class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:       # because, 0*0 = 0 and 1*1 = 1
            return x
        # binary search, but with integers instead of an array
        left = 0
        right = x // 2
        while left <= right:
            middle = (left + right) // 2
            square = middle * middle
            if x < square:              # here x is the 'target' to match in
                right = middle - 1      # the usual binary search
            elif x > square:
                left = middle + 1
            else:
                return middle
        return right
