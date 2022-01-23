import java.util.*;

public class FrogMinCost {
    public static void main(String[] args) {
        int[] heights = new int[]{30,10,60,10,60,50};
        int n = heights.length;

        System.out.println("The minimum cost for the frog to reach from 0 to N is: "+ frogJump(n, heights));
    }

    static int frogJump(int n, int[] heights) {
        int[] minCost = new int[n];
        Arrays.fill(minCost, -1);
        minCost[0] = 0;
        minCost[1] = Math.abs(heights[0] - heights[1]);
        for (int i = 2; i < n; i++){
            minCost[i] = Math.min(minCost[i-1] + Math.abs(heights[i-1] - heights[i]), 
                                    minCost[i-2] + Math.abs(heights[i-2] - heights[i]));
        }
        return minCost[n-1];
    }
}
