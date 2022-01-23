import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Day8 {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = in.nextInt();

        HashMap<String, Integer> pb = new HashMap<>();
        ArrayList<String> queries = new ArrayList<>();
//        String[] st = new String[2];
//        int[] it = new int[2];

        for (int i = 0; i < n; i++) {
            pb.put(in.next(), in.nextInt());
//            st[i] = in.next();
//            it[i] = in.nextInt();
        }

        in.nextLine();
        String str;
        int noq = 0;
        while(in.hasNext()){
            str = in.next();
            queries.add(str);
            noq++;
        }


        for (int i=0; i<noq; i++){
            str = queries.get(i);
            if(pb.containsKey(str))
                System.out.println(str+"="+pb.get(str));
            else
                System.out.println("Not found");
        }
    }
}