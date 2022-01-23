


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//Taking input without specified limit
//MULTIPLE LINES 
public class UnspecifiedMultiLineInput{

    static void readInput(ArrayList<Integer> numbers) throws IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String input;
        do{
            input = in.readLine();
            if(input.length() > 0)
                for(String str : input.split(" "))
                    numbers.add(Integer.valueOf(str));         
            else
                break;
        }while(true);
    }
    public static void main(String[] args) throws IOException{
        
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        readInput(numbers);
        System.out.println("\n"+numbers);
    }
}


