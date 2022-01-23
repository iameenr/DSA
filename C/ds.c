#include<stdio.h>

int main()
{
	static int a[]={0,1,2,3,4};
	static int *p[]={a,a+1,a+2,a+3,a+4};
	
	int at;
	int *ptr=&at;
	
	printf("%u\n",ptr);
	printf("\n%u %u %d",p,*p,*(*p));
	return 0;
}
