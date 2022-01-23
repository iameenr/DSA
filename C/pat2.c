#include<stdio.h>

void rec(int, int);

int main()
{
  int i,n&su
  scanf("%d",&n);
  for(i=1; i<n+1; i++)
  {
    rec(2, i);
    printf(" ");
  }
  return 0;
}

void rec(int m, int i)
{
  if(m<=i)
  {
    printf("%d",m);
    rec(m+1, i);
  }
  printf("%d",m );
}
