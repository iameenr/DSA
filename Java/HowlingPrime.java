import java.io.*;
import java.util.Scanner;
import java.lang.Math;

public class HowlingPrime
{
	public static void  main(String args[])
	{	
		int sod=0;
		boolean flag=true;
		
		Scanner inp=new Scanner(System.in);
		int no=inp.nextInt();
		while(no!=0)
		{
		sod=sod+(no%10);
		no=no/10;
		}
		
		check:
		{
			if(sod%2==0)
			{
				flag=false;
				break check;
			}
			double mid=Math.ceil(Math.sqrt(no));
			for(int i=3;i<=mid;++i)
			{
				if(sod%i==0)
				{
					flag=false;
					break check;
				}
				++i;
			}
		}
		
		if(flag)
			System.out.println("IS a Howling Prime");
		else
			System.out.println("NOT a Howling Prime");
	}
}

	