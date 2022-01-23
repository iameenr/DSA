#include <stdlib.h>
#include <math.h>
#include <stdio.h>

#define maxexp 100                 //the max expr length can be 100
char expr[maxexp],sol[20];

void analyze(char *expr);         //Function to analyze the expr

int main()
{
  int i,j,k;
  char c;

  inp:
  {
    for(i=0;c!='=';i++)
    {
      scanf(" %c",&c);
      expr[i]=c;
      //exp+=1;
    }
    expr[i-1]='\0';
  }

  for(j=0;expr[j]!='\0';j++)          //VERIFIED
    printf("%c",expr[j]);

  analyze(expr);

  return 0;
}

void analyze(char *expr)
{
  int j;
  printf("\n");
  for(j=0;expr[j]!='\0';j++)          //VERIFIED
    printf("%c",expr[j]);

  printf("\n");
  for(j=0;expr[j]!='\0';j++)
  {
    if(isalpha(expr[j]))
      printf("alpha\n");
    else if(expr[j]==' ')
      continue;
    else
      printf("NUM\n");
  }
  return;
}
