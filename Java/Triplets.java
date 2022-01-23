public class Triplets {
        public int[] twoSum(int[] nums, int tripleTarget) {
            HashMap<Integer, Integer> map = new HashMap<>();
            int target;
            for(int j=0;j<nums.length;j++) {
                target = tripleTarget - nums[j];
                for (int i = 0; i < nums.length; i++) {
                    diff = target - nums[i];
                    if (map.containsKey(diff))
                        return new int[]{j, map.get(diff), i};
                    else
                        map.put(nums[i], i);
                }

                map.clear();
            }
            return new int[]{0, 0, 0};
        }
    }

