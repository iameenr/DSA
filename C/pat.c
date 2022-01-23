#include<stdio.h>
int main()
{
  int n,i,j,k;
  scanf("%d",&n);


//printf("2 ");
for(i=1;i<n+1;i++)
{
  for(j=2;j<=i;j++)
  {
    printf("%d",j);
  }
  for(k=j;k>=2;k--)
  {
    printf("%d",k);
  }
  printf(" ");
}

return 0;
}
