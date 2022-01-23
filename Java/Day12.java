import java.util.ArrayList;
import java.util.Scanner;
public class Day12 {
    public static void main(String[] args) {
        Person p = new Person();
        p.readInfo();

        Student s = new Student();
        s.readMarks();
        char grade = s.calculate();

        p.printDetails();
        System.out.println("Grade: "+grade);
    }
}

class Person {
    String fname, lname;
    int id;
    Scanner in = new Scanner(System.in);
    void readInfo(){
        fname = in.next();
        lname = in.next();
        id = Integer.parseInt(in.next());
    }

    void printDetails() {
        System.out.println(lname + ", " + fname);
        System.out.println("ID: "+id);
    }
}

class Student extends Person{
    private int id;
    int n;
    ArrayList<Integer> marks = new ArrayList<>();
    Scanner in = new Scanner(System.in);

    void readMarks(){
        n = in.nextInt();
        for(int i=1; i<=n; i++)
            marks.add(in.nextInt());
    }

    char calculate(){
        int sum = 0;
        for(int i=0; i<n; i++){
            sum += marks.get(i);
        }
        int a = sum/n;

        if(a<40)
            return 'T';
        else if(a>=40 && a<55)
            return  'D';
        else if(a>=55 && a<70)
            return  'P';
        else if(a>=70 && a<80)
            return  'A';
        else if(a>=80 && a<90)
            return  'E';

        return  'O';
    }
}
