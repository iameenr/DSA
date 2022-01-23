class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        ArrayList<Integer> numbers = new ArrayList<>();
        for(int num : nums){
            numbers.add(num);
        }
        
        Collections.sort(numbers);
        
        List<List<Integer>> result = new ArrayList<>();

        int target = 0;
        int smallerIndex = 0, biggerIndex = 0;
        int sum=0, len =  numbers.size();
        for (int i = 0; i < len-2; i++) {
            smallerIndex = i+1;
            biggerIndex = len - 1;
            while(smallerIndex!= biggerIndex) { 
                
                sum = numbers.get(i) + numbers.get(smallerIndex) + numbers.get(biggerIndex);
                if(sum < target)
                    smallerIndex++;
                else if(sum > target)
                    biggerIndex--;      
                else{
                    ArrayList<Integer> combination = new ArrayList<>();
                    combination.add(numbers.get(i)); combination.add(numbers.get(smallerIndex)); combination.add(numbers.get(biggerIndex));
                    if(!result.contains(combination))
                        result.add(combination);
                    biggerIndex--;
                }
            }
        }
        return result;
    }
}