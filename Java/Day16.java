import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;



public class Day16 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String S = bufferedReader.readLine();
        bufferedReader.close();

        try {
            int n = Integer.parseInt(S);
            System.out.println(n);
        }
        catch (NumberFormatException e){
            System.out.println("Bad String");
        }
    }
}
