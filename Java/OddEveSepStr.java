import java.util.ArrayList;
import java.util.Scanner;

public class OddEveSepStr {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int notc = sc.nextInt();
        sc.nextLine();

        String str;
        ArrayList<String> inps = new ArrayList<String>();
        for (int i = 0; i < notc; i++)
            inps.add(sc.nextLine());

        for (int i = 0; i < notc; i++) {
            str = inps.get(i);
            int j = 0;
            while (j < str.length()) {
                System.out.print(str.charAt(j));
                j = j + 2;
            }

            System.out.print(" ");

            j = 1;
            while (j < str.length()) {
                System.out.print(str.charAt(j));
                j = j + 2;
            }
            System.out.println("");
        }
    }
}