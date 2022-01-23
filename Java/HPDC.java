import java.io.*;
import java.util.Scanner;
import java.lang.Math;

class DC
{
		int Sum_of_digits(int no)
		{
			int sod=0;
			while(no!=0)
			{
				sod=sod+(no%10);
				no=no/10;
			}
			return sod;
		}
		
		boolean Is_Prime(int n)
		{
			boolean flag=true;
			check:
			{
				if(n%2==0)
				{
					flag=false;
					//System.out.println("Not a prime, ");
					break check;
				}
				double mid=Math.ceil(Math.sqrt(n));
				for(int i=3;i<=mid;++i)
				{
					if(n%i==0)
					{
						flag=false;
						//System.out.println("Not a prime, ");
						break check;
					}
					++i;
				}
			}		
			return flag;
		}
}

public class HPDC
{
	public static void main(String args[])
	{
		Scanner inp=new Scanner(System.in);
		int no=inp.nextInt();
		 
		DC obj=new DC();
		if(obj.Is_Prime(no) && (obj.Is_Prime(obj.Sum_of_digits(no))))
			System.out.println("Is a Howling Prime");
		else
			System.out.println("Not a Howling Prime");
	}
}	