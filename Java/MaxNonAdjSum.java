public class MaxNonAdjSum {
    public static void main(String[] args) {
        int[] arr = new int[]{5, 5, 10, 100, 10, 5};

        System.out.println("Answer = "+ CalMax(0, arr, 0));
    }

    static int CalMax(int index, int[] arr, int MaxNow){
        int[] dp = new int[arr.length];
        dp[0] = arr[0];
        dp[1] = Math.max(dp[0], arr[1]);
        
        for (int i = 2; i < dp.length; i++) {
            dp[i] = Math.max(dp[i-1], dp[i-2] + arr[i]);
        }
        
        return dp[arr.length - 1];
        // System.out.println("Here "+index);
        // if(index >= arr.length) return MaxNow;
        // return Math.max(CalMax(index+2, arr, MaxNow + arr[index]),
        //                     CalMax(index+1, arr, MaxNow));
    }
}
