import java.util.ArrayList;
import java.util.Scanner;
import java.lang.Math;

public class MaxPath {
    static int row, col;
    static int MaxPath = 0;
    public static void main(String[] args) {
        Scanner in =  new Scanner(System.in);
        row = in.nextInt(); col = in.nextInt();

        ArrayList<Integer> rows = new ArrayList<>();
        ArrayList<ArrayList<Integer>> mat = new ArrayList<>();

        for(int j=0; j<row; j++){
            for(int i=0; i<col; i++)
                rows.add( in.nextInt());
            mat.add(rows);
            rows = new ArrayList<>();
            }
        System.out.println(mat);
        System.out.println(MaxPathFinder(MaxPath,0, 0, mat));
        }

        static int MaxPathFinder(int MaxPath,int r, int c, ArrayList<ArrayList<Integer>> mat){
            if(r<row && c<col)
                MaxPath += mat.get(r).get(c);
            else
                return MaxPath;
//            System.out.println(MaxPath);
            MaxPath = Math.max(MaxPathFinder(MaxPath,r+1, c, mat), MaxPathFinder(MaxPath, r, c+1, mat));
//            System.out.println(MaxPath);
            return MaxPath;
        }

    }
