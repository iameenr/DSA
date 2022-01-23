import java.util.ArrayList;
import java.util.Scanner;
import java.lang.Math;

public class MaxHG {
    public static void main(String[] args) {

        ArrayList<ArrayList<Integer>> twodm = new ArrayList<>();
        ArrayList<Integer> row1 = new ArrayList<>();
        ArrayList<Integer> row2 = new ArrayList<>();
        ArrayList<Integer> row3 = new ArrayList<>();
        ArrayList<Integer> row4 = new ArrayList<>();
        ArrayList<Integer> row5 = new ArrayList<>();
        ArrayList<Integer> row6 = new ArrayList<>();

        Scanner in = new Scanner(System.in);

        for (int j = 0; j < 6; j++)
            row1.add(in.nextInt());
        twodm.add(row1);

        for (int j = 0; j < 6; j++)
            row2.add(in.nextInt());
        twodm.add(row2);

        for (int j = 0; j < 6; j++)
            row3.add(in.nextInt());
        twodm.add(row3);

        for (int j = 0; j < 6; j++)
            row4.add(in.nextInt());
        twodm.add(row4);

        for (int j = 0; j < 6; j++)
            row5.add(in.nextInt());
        twodm.add(row5);

        for (int j = 0; j < 6; j++)
            row6.add(in.nextInt());
        twodm.add(row6);

//        for(int i=0; i<6; i++) {
//            for (int j = 0; j < 6; j++)
//                System.out.print(twodm.get(i).get(j) + " ");
//            System.out.println();
//        }


        int sumofthishourglass = 0, maxsum = 0;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                for(int k=0; k<3; k++){
                    sumofthishourglass += twodm.get(i).get(k+j);
                    if(k == 1)
                        sumofthishourglass += twodm.get(i+1).get(k+j);
                    sumofthishourglass += twodm.get(i+2).get(k+j);
                }

                if (i == 0 && j == 0)
                    maxsum = sumofthishourglass; // To manage negatives

                maxsum = Math.max(maxsum, sumofthishourglass);
                sumofthishourglass = 0;
            }
        }

        System.out.println(maxsum);
    }
}
