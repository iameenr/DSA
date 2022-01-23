#include<stdio.h>

main()
{
   int i = 1;

   Charminar:
   printf("%d ",i++);
   if(i==3)
    break;
   if(i<=5) goto Charminar;
}
