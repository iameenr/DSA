import java.util.*;

public class altchar {

    public static void main(String[] args) {
        String s;
        String res = "";
        int sum = 0;
        Scanner in = new Scanner(System.in);
        s = in.nextLine();
//        System.out.println(s);
//        int ch = (int)s.charAt(0);
//        System.out.println(ch);
        int i=0;
        while (i<s.length()){
            int c = (int)s.charAt(i);
            if(c >= 48 && c <= 57) {
                int cc = (int)s.charAt(i + 1);
                if (cc >= 48 && cc <= 57) {
                    sum = sum + (((c - 48) * 10)) + cc - 48;
                    i += 2;
                }
                else {
                    sum +=  c - 48;
                    i += 1;
                }
            }
            else {
                res += (char)c;
                i += 1;
            }
        }
        System.out.println(sum);
        System.out.println(res);
        }
    }
