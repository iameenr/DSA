import java.io.*;
import java.util.*;

class Person{
    private int age;

    public Person(int initialAge){
        this.age=initialAge;
    }

    void amIOld(){
        if( age<0 ){
            System.out.println("Age is not valid, setting age to 0.");
            age = 0;
            System.out.println("You are young.");
        }
        else if( age<13 )
           System.out.println("You are young.");
        else if( age<18 )
            System.out.println("You are a teenager.");
        else
            System.out.println("You are old.");
    }

    void yearPasses(){
        age+=1;
    }

}

public class Day4 {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int noa = sc.nextInt();
        int[] InitialAge = new int[noa];
        Person p;

        for(int i=0; i<noa; i++){
            InitialAge[i] = sc.nextInt();
        }

        for(int i=0; i<noa; i++){
            p = new Person(InitialAge[i]);
            p.amIOld();

            for(int j=1;j<=3;j++)
                p.yearPasses();
            
            p.amIOld();
            System.out.println("");
        }
    }

}