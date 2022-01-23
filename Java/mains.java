
import java.util.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class mains {
    public static void main(String[] args) {
        Sorter sorter = new Sorter();
        sorter.AlternateSort();
    }
}


class Sorter {
    private List<Integer> list = new ArrayList<>();

    void AlternateSort(){
        Scanner in = new Scanner(System.in);
        while(in.hasNext())
            list.add(in.nextInt());

        Collections.sort(list);
        System.out.println(list);
    }
}
