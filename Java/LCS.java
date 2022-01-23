import java.util.*;
import java.lang.Math.*;

public class LCS
{
    public static void main(String args[]){
        String s1= "Maragadha Naanayam";
        String s2= "Naana Thaana Veena Pona";
        int CIndex=0, CLength = 0, LL = 0;

        for ( int i=0; i<s1.length(); i++){
            for ( int j=0; i<s1.length() && j<s2.length(); j++){

                if( s1.charAt(i) == s2.charAt(j)){
                    //Substring search begins

                    if( CLength == 0 ){
                        CLength = 1;
                        CIndex = i;
                        i+=1;
                        System.out.println("\nSubstring search begins | " +s1.charAt(i));
                        continue;
                    }
                    else{
                        CLength += 1;
                        i+=1;   
                    }
                }
                else if(CLength > 0){
                    LL = Math.max(LL, CLength);
                    System.out.println("Current Index " +s1.charAt(CIndex));
                    System.out.println("Max Index " +i);
                    System.out.println("Max Length " +CLength);

                    i = CIndex + 1;;
                    j = 0;
                    CLength = 0;
                    
                }

                else
                    continue;

            }
        }

        System.out.println(s1.charAt(10));
        System.out.println(LL);
        System.out.println(CIndex);
        System.out.println(CLength);

    }
}