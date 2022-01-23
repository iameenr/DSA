import java.util.ArrayList;
import java.util.Scanner;

public class UniquePal {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.nextLine();

        ArrayList<String> substr = new ArrayList<>();
        String temp = "";
        for(int m = 0; m<s.length(); m++) {
            for (int i = 0; i < s.length(); i++) {
                for (int j = m; j <= i; j++) {
                    temp += s.charAt(j);
                }
                if (!substr.contains(temp))
                    substr.add(temp);
                temp = "";
            }
        }

//        System.out.println(substr);

        String check;
        for (int i = 0; i < substr.size(); i++) {
            check = substr.get(i);
            if(isPal(check))
                System.out.print(check+ " ");
        }

        System.out.println("");
    }

    static Boolean isPal(String check){
        int n = check.length();
        for(int i=0; i<n/2; i++){
            if(!(check.charAt(i) == check.charAt(n-i-1)))
                return false;
        }
        return true;
    }
}
