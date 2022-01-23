import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'minimumBribes' function below.
     *
     * The function accepts INTEGER_ARRAY q as parameter.
     */

    public static void minimumBribes(List<Integer> q) {
        // Write your code here
        int n = q.size();
        int tnob = 0;
        int expf = 1;
        int exps = 2;
        int expt = 3;

        for(int i=0; i<n; i++){
            if(q.get(i) == expf){
                expf = exps;
                exps = expt;
                ++expt;
            }
            else if(q.get(i) == exps){
                exps = expt;
                ++expt;
                tnob+=1;
            }
            else if(q.get(i) == expt){
                ++expt;
                tnob+=2;
            }
            else {
                System.out.println("Too chaotic");
                return;
            }
        }
        System.out.println(tnob);
        return;
    }

}

public class BribingQueue{
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                int n = Integer.parseInt(bufferedReader.readLine().trim());

                List<Integer> q = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList());

                Result.minimumBribes(q);
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
    }
}
