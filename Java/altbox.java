import java.util.*;
import java.lang.*;

public class altbox
{
    public static void main(String[] args)
    {
        int n=5;
        int[][] m = new int[n][n];
        
        for(int row=0; row < n; row++){
                if( row%2 == 0){
                    for(int col=0; col < n; col++){
                        System.out.println("Setting "+row+col +" to one.");
                        m[row][col] = 1;
                        m[n-1-row][col] = 1;

                        m[col][row] = 1;
                        m[col][n-1-row] = 1;
                    }
                }

                if( row%2 == 1){
                    for(int col=row; col < n ; col++){
                        System.out.println("Setting "+row+col +" to zero.");
                        m[row][col] = 0;
                        m[n-1-row][col] = 0;

                        m[col][row] = 0;
                        m[col][n-1-row] = 0;
                    }

                }
        }


        for(int row=0; row < n; row++){
            for(int col=0; col < n; col++)
                System.out.print(m[row][col]+" ");
            System.out.println("");
        }

    }
}
