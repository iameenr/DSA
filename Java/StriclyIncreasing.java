class Solution {
    public boolean canBeIncreasing(int[] nums) {
        //loop through nums and find only one mismatched solution

        int count = 0;
        for (int i = 1; i < nums.length && count != 2; i++) {
            if(nums[i] < nums[i-1]){
                count++;
            }
        }

        return count == 1;
    }
}