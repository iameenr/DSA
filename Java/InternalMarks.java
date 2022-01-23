import java.io.*;
import java.util.*;

public class InternalMarks
{
	public static void main(String args[])
	{
		int n;
		Scanner sc=new Scanner(System.in);
		
		System.out.println("Enter the number of students: ");
		n=sc.nextInt();
		
		calculation(n);
	}
	
	static void calculation(int n)
	{
		int i=1;
		double att_perc,int_marks=0.0;
		
		Scanner in=new Scanner(System.in);
		while(i<=n)
		{
			System.out.print("Enter the attendence percentage of Student "+i +": ");
			att_perc=in.nextDouble();
		
			if(att_perc<75.0){
				int_marks=0.0;
			}
			else if(att_perc>=75.0 && att_perc<80.0){
				int_marks=5.0;
			}
			else if(att_perc>=80.0 && att_perc<85.0){
				int_marks=10.0;
			}
			else if(att_perc>=85.0 && att_perc<90.0){
				int_marks=15.0;
			}
			else if(att_perc>=90.0 && att_perc<100){
				int_marks=20.0;				
			}
		
			System.out.println("Internal marks of student "+i+" is = "+int_marks);
			i++;
		}
	}
}