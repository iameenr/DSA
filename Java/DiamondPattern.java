import java.io.*;
import java.util.*;

public class DiamondPattern {
    public static char[][] m = new char[100][100];
        

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int noi;
        Scanner sc = new Scanner(System.in);
        noi = sc.nextInt();
        int[][] inputs = new int[noi][3];
        for(int i=0; i<noi; i++){
            for(int j=0; j<3; j++){
                inputs[i][j]= sc.nextInt();
            }
        }

        for(int i=0; i<noi; i++){
            int k=0;
            int j=0;
            Diamond(inputs[i][j+2]);
            int dis=inputs[i][j+2]*2;

            for(j=0; j<inputs[i][0]; j++){
                if(inputs[i][k+1] > 1){
                    for(int r=0; r<dis; r++){
                        for(int rep=0; rep<inputs[i][k+1]; rep++){
                            for(int c=0; c<dis; c++){
                                System.out.print(m[r][c]+" ");
                            }
                        }
                        System.out.println("");
                    }
                }
                else{
                    for(int r=0; r<dis; r++){
                        for(int c=0; c<dis; c++){
                            System.out.print(m[r][c]+" ");
                        }
                    System.out.println("");
                    } 
                }  
            }
        }
    }

    static void Diamond(int n){
        int dis=n*2;
        for(int r=0; r<dis; r++)
            for(int c=0; c<dis; c++)
                m[r][c] = '.';
            

        for(int row=0; row<n; row++){
            int col=0;
                while ( col<n-1-row){
                    m[row][col] = '.';
                    col++;
                }

                m[row][col] = '/';
                m[dis-1-row][col] = '\\';
                col++;

                for(int i=0; i<2*row; i++){
                    m[row][col] = '*';
                    m[dis-1-row][col] = '*';
                    col++;
                }

                m[row][col] = '\\';
                m[dis-1-row][col] = '/';

        }

       
    }
        
}
