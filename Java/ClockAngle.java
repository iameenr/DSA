import java.io.*;
import java.util.*;
import java.text.*;

public class ClockAngle {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        double hour, minute, angle;
        int aph = 30;
        int apm = 6;

        Scanner sc = new Scanner(System.in);
        hour = sc.nextInt();
        minute = sc.nextInt();

        double minuteangle = minute*apm;
        double hourangle = hour*aph + minute*0.5;

        angle = hourangle - minuteangle;
        if(angle<0)
            angle*=-1;

        DecimalFormat df = new DecimalFormat("0.000000");

        if(angle > 180)
            System.out.println(df.format(360-angle));
        else
            System.out.println(df.format(angle));


    }
}