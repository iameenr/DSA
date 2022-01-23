#include<stdio.h>

int main()
{
	int no_of_segments,max_point;
	int points[200],no_of_points;
	long array[45000];
	int i,k,j,count=0;
	
	scanf("%d",&no_of_segments);
	scanf("%d",&max_point);
	
	for(i=0;i<max_point;i++)
	{
		array[i]=1; 		//1 -> True
	}
	array[i]=3;
	
	no_of_points=no_of_segments*2;
	for(i=0;i<no_of_points;i++)
	{
		scanf("%d",&points[no_of_points]);
	}
	
	for(k=0;k<max_point;k+2)
	{
		j=k;
		for(i=points[k];i<=points[k+1];i++)
		{
			array[(points[j])-1]=0;
			j++;
		}
	}
	
	for(i=0;i<max_point;i++)
	{
		if(array[i]!=3)
		{
			if(array[i]!=0)
			{
			count=count+1;
			}
		}
			
	}
	
	for(i=0;i<max_point;i++)
	{
		
}