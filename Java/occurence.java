import java.util.Scanner;

public class occurence {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        int range = in.nextInt();

        int count = 0;
        for (int n = 1; n <= range ; n++) {
            count += noOfOccurence(num, n);
        }
        System.out.println(count);
    }

    static int noOfOccurence(int num, int n){
        int count = 0;
        for(int i=0; n>0; i++) {
            if (num == n % 10)
                count++;
            n = n/10;
        }
        return count;
    }
}


