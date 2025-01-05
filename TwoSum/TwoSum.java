class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ret = {0, 0};
        for (int j=0; j < nums.length; j++) {
            ret[0] = j;
            for (int i=0; i < nums.length; i++) {
                if(j != i) {
                    if(nums[j] + nums[i] == target) {
                        ret[1] = i;
                        return ret;
                    }
                }
            }
        }
        return ret;
    }
}
