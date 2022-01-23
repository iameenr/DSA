import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


class Difference {
    private int[] elements;
    public int maximumDifference;

    Difference(int[] elements){
        this.elements = elements;
    }

    void computeDifference(){
       int maxEle = elements[0], minEle = elements[0];

        for (int i = 1; i < elements.length; i++) {
            minEle = Math.min(minEle, elements[i]);
            maxEle = Math.max(maxEle, elements[i]);
        }
        maximumDifference = Math.abs(maxEle - minEle);
    }

} // End of Difference class


class  Day14{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int ele[] = new int[n];
        for (int i = 0; i < n; i++)
            ele[i] = in.nextInt();

        Difference d = new Difference(ele);
        d.computeDifference();
        System.out.println(d.maximumDifference);

    }
}
