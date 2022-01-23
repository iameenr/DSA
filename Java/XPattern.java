import java.util.*;
import java.lang.*;

public class XPattern
{
    public static void main(String[] args)
    {
        String word = new String();
        Scanner sc = new Scanner( System.in );
        word = sc.nextLine();

        // System.out.println(word);
        int n = word.length();
        for (int i=0; i<=n/2; i++){
            for(int s=0; s<i; s++)
                System.out.print(" ");

            System.out.print(word.charAt(i));

            for(int s=0; s<(n-2)-(i*2); s++)
                System.out.print(" ");

            if( (n-1-i)!= n/2)
                System.out.print(word.charAt(n-1-i));
            System.out.println("");
        }

        for(int i=n/2-1; i>=0; i--){
            for(int s=0; s<i; s++)
                System.out.print(" ");

            System.out.print(word.charAt(i));

            for(int s=0; s<(n-2)-(i*2); s++)
                System.out.print(" ");

            System.out.print(word.charAt(n-1-i));
            System.out.println("");
        }

    }

}












