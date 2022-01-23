//DOESN'T WORK. ITS A MESSY, WRONG SOLUTION


class Solution {
    public int longestMountain(int[] arr) {
        int lengthOfArray = arr.length, length = 0, maxLength = 0;
        boolean incr, decr, mountain = false;

        //seeing if it's initially increasing or decreasing
        if(lengthOfArray < 3)
            return 0;
        else if(arr[1] > arr[0]){ incr = true; decr = false; length = 2;}
        else {incr = false; decr = true;}

        //Looping through entire array to find peaks and count meanwhile
        for(int i=1; i<=lengthOfArray-2; i++){
            if(arr[i+1] > arr[i]){
                if(incr)
                    length++;
                if(decr)
                {
                    if(mountain){
                        maxLength = Math.max(maxLength, length++);
                        length = 2;
                        incr = true; mountain = false;
                    }
                    else{ incr = true; decr = false; mountain = false; length = 2; }
                }
                if(!incr && !decr){
                    incr = true; decr = false; length = 2;
                }

            }
            else if(arr[i+1] == arr[i]){
                if(mountain){
                    maxLength = Math.max(maxLength, length++);
                    length = 2;
                    incr = false; decr = false; mountain = false;
                }
                else
                    length = 0;
            }
            else{
                if(incr){ incr = false; decr = true; mountain = true; }
                length++;
            }
        }
        return maxLength;
    }

   
  