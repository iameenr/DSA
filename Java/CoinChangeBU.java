import java.util.*;
import java.math.*;

class CoinChangeBU {
    public static void main(String[] args) {
        int[] denomination = new int[]{1,4,7,10};
        int target = 14;

        System.out.println("Minimum number of coins required to make change of "+target+" is "+ minCoins(target, denomination));
    }

    static int minCoins(int target, int[] denomination){
        int[] change = new int[target+1];
        change[0] = 0;
        for (int i = 1; i < change.length; i++) {
            change[i] = Integer.MAX_VALUE;
            for(int coin : denomination){
                if(i - coin >= 0 &&  change[i-coin] != Integer.MAX_VALUE)
                    change[i] = Math.min(change[i], change[i-coin] + 1);
            }
        }
        return change[target] == Integer.MAX_VALUE ? -1 : change[target];
    }
}
