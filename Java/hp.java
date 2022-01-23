import java.io.*;
import math.h;

public class HowlingPrime
{
	public static void  main(string args[])
	{	
		int sod=0;
		Scanner inp=new Scanner(System.in);
		int no=sc.nextInt();
		
		while(no!=0)
		{
		sod+=no%10;
		no=no/10;
		}
		
		check:
		{
			if(no%2==0)
			{
				System.out.println("Not a Howling Prime");
				break check;
			}
			int mid=ceil(sqrt(no));
			for(int i=3;i<=mid;i=i+2)
			{
				if(no%i==0)
				{
					System.out.println("Not a Howling Prime");
					break check;
				}
			}
		}
		System.out.println("Is Howling Prime");
	}
}

	