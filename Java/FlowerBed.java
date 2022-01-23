class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int flowerbedLength = flowerbed.length;
        int count = 0, prev = 0, next;
        
        for (int i = 0; i < flowerbedLength; i++) {
            if(flowerbed[i] == 0){
                prev = (i==0)? 0:flowerbed[i-1];
                next = (i==flowerbedLength-1)? 0:flowerbed[i+1];
                if(prev == 0 && next == 0){
                    count++; 
                    flowerbed[i] = 1;
                }
            } 
        }
        return n<=count;
    }
}