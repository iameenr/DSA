import java.util.*;
import java.lang.*;

public class XPatternUsingWhile
{
    public static void main(String[] args)
    {
        String word = new String();
        Scanner sc = new Scanner( System.in );
        word = sc.nextLine();

        // System.out.println(word);
        int n = word.length();
        int i=0;
        boolean forward = true;
        while( i>=0){
            for(int s=0; s<i; s++)
                System.out.print(" ");

            System.out.print(word.charAt(i));

            for(int s=0; s<(n-2)-(i*2); s++)
                System.out.print(" ");

            if( (n-1-i)!= n/2)
                System.out.print(word.charAt(n-1-i));
            else
                forward = false;
            System.out.println("");

            if( forward ) i++;
            else i--;
        }

    }

}












