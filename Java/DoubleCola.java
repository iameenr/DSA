import java.util.ArrayList;
import java.util.Scanner;

public class DoubleCola {
    public static void main(String[] args) {
        ArrayList<String> queue = new ArrayList<>();
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        queue.add("Sheldon");
        queue.add("Leonard");
        queue.add("Penny");
        queue.add("Rajesh");
        queue.add("Howard");
        int front = 0;
        for(int i=5; i<n; i=i+2){
            queue.add(i, queue.get(front));
            queue.add(i+1, queue.get(front));
            front++;
        }

        System.out.println(queue);
        System.out.println(queue.get(n-1));
    }

}
