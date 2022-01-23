class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int diff;
        for(int i=0; i<nums.length; i++){
            diff = target - nums[i];
            if(map.containsKey(diff))
                return new int[]{map.get(diff),i};
            else
                map.put(nums[i],i);
        }
        return new int[]{0, 0};
    }
}