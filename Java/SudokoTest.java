import java.util.*;
import java.lang.*;

public class SudokoTest
{
    public static void main(String[] args)
    {
        int[][] m = new int[9][9];
        Scanner sc = new Scanner(System.in);

        int tc = sc.nextInt();
        boolean[] tcres = new boolean[tc];

        Solution resobj = new Solution();

        for(int k=0; k<tc; k++){

            for(int i=0; i<9; i++)
                for(int j=0; j<9; j++)
                    m[i][j] = sc.nextInt();
            
            tcres[k] = resobj.IsSudoko(m);    
        }

        // System.out.println("");

        // for(int i=0; i<9; i++){
        //     for(int j=0; j<9; j++)
        //     System.out.print(m[i][j]+" ");
        // System.out.println("");
        // }
            
            

        // ArrayList< HashMap< Integer, Integer>> lomaps = new ArrayList<HashMap< Integer, Integer>>();
       for (int i=0; i<tc; i++){
            if(tcres[i])
                System.out.println("Valid");
            else    
                System.out.println("Invalid");
       }
    }
}

class Solution
{
    boolean IsSudoko(int[][] m){
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int ce;

        for (int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                ce = m[i][j];
                if( map.containsKey(ce) )
                    return false;
                else
                    map.put(ce, 1);
            }
            map.clear();
        }

        map.clear();
        for (int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                ce = m[j][i];
                if( map.containsKey(ce) )
                    return false;
                else
                    map.put(ce, 1);
            }
            map.clear();
        }

        map.clear();
        int g=3;
        int j, i;
        for(int t=0; t<9; t++){
            for( i=(t/3)*3 ; i< ((t/3)+1)*3; i++){
                for( j=(t%3)*3; j<g; j++){
                    ce = m[i][j];
                    if( map.containsKey(ce)){
                        // System.out.println("Wrong Answer at " +i+j);
                        return false;
                    }
                    else
                        map.put(ce, 1);
                }
            }
            // System.out.println("Clearing Grid " +(t+1));
            map.clear();
            if( g==9 )
                g=3;
            else
                g = (g+3);
        }

        return true;
    }
}