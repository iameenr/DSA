//Sum of three numbers in an aray that equate to a target number
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class UnspecifiedOneLineInput{
    public static void main(String[] args) throws IOException{
        //Taking input without specified limit
        //ONE LINE ONLY 
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String input = in.readLine();
        for(String str : input.split(" ")){
            numbers.add(Integer.valueOf(str));
        }
        System.out.println(input+"\n"+numbers);

        // numbers = input.stream().map(Integer::valueOf).collect(Collectors.toList())
    }
}
