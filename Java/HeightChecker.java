//Counting Sort
class Solution {
    public int heightChecker(int[] heights) {
        int[] FrequencyOfHeight = new int[101];
        
        for (int height : heights) {
            FrequencyOfHeight[height]++;
        }
        
        int WrongPosition = 0;
        int curHeight = 0;
        
        for (int i = 0; i < heights.length; i++) {
            while (FrequencyOfHeight[curHeight] == 0) {
                curHeight++;
            }
            
            if (curHeight != heights[i]) {
                WrongPosition++;
            }
            FrequencyOfHeight[curHeight]--;
        }
        
        return WrongPosition;
    }
}