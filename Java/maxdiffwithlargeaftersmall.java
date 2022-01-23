import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


class Diff {
    private int[] elements;
    public int maximumDifference;

    Diff(int[] elements){
        this.elements = elements;
    }

    void computeDifference(){
        int maxEle = elements[0], minEle = elements[0];
        int prevminpos = 0, prevmaxpos = 0;
        int maximumDifferenceNow = 0;

        for (int i = 1; i < elements.length; i++) {
           if(elements[i] < minEle){
              minEle = elements[i];
              prevminpos = i;
           }
           if(elements[i] > maxEle){
               maxEle = elements[i];
               prevmaxpos = i;
           }
            if(prevminpos < prevmaxpos) {
                maximumDifferenceNow = elements[prevminpos] - elements[prevmaxpos];
                maximumDifference = Math.max(maximumDifference, Math.abs(maximumDifferenceNow));
            }
        }

    }

} // End of Difference class


public class  MaxDiffWithLargeAfterSmall{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int ele[] = new int[n];
        for (int i = 0; i < n; i++)
            ele[i] = in.nextInt();

        Diff d = new Diff(ele);
        d.computeDifference();
        System.out.println(d.maximumDifference);

    }
}
