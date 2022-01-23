import java.util.ArrayList;
import java.util.Scanner;
public class ques2{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s1, s2;
        s1 = in.next();
        s2 = in.next();

        ArrayList<Character> cs1 = new ArrayList<>();
        ArrayList<Character> cs2 = new ArrayList<>();

        for(int i=0; i<s2.length(); i++){
            cs2.add(s2.charAt(i));
        }

        for(int i=0; i<s1.length(); i++){
            char c = s1.charAt(i);
            if(!cs2.contains(c))
                cs1.add(c);
        }

        for (int i = 0; i < cs1.size(); i++) {
            System.out.print(cs1.get(i));
        }

        System.out.println("");

    }
}
