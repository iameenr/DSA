import java.util.Scanner;

//90:02:18:FF:BC:F6
//        output =900218FFBCF6

public class Tests {
    public static void main(String[] args) {
        String str;
        Scanner in = new Scanner(System.in);
        str = in.nextLine();
//
//        int hex = Integer.parseInt(str, 16);
//
//
//        System.out.print("Output = "+hex);
        int flag = 0;
        for (int i=0; i<str.length(); i++){
            char ch = str.charAt(i);
            if( ch=='f' &&( (int)str.charAt(i+1)>=48 && (int)str.charAt(i+1)<=57 )){
                char next = (char)((int)str.charAt(i+1) - 2);
                System.out.println("f"+next);
                flag = 1;
                continue;
            }
            if( ch !=':' && flag == 0)
                System.out.print(ch);
            }
        }
    }


