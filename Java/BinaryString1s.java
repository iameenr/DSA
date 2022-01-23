import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class BinaryString1s {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());

        Stack<Integer> st = new Stack<>();

        int len=0;
        while( n>0 ){
            st.push( n%2 );
            n/=2;
            len+=1;
        }

        int onesnow=0, maxones=0;
        while( !st.isEmpty() ){
            if( st.pop() == 1)
                onesnow+=1;
            else {
                maxones = Math.max(onesnow, maxones);
//                System.out.print(maxones + ".");
                onesnow = 0;
            }
        }
        maxones = Math.max(onesnow, maxones);
        System.out.println(maxones);
    }
}
