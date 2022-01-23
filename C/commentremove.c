#include <stdio.h>
#define max 720

char line[max];
int getline(char S[],int limit);

main()
{
  int check,i,m;

  printf("Enter your program below: \n");
  while((check=getline(line,max))>0)
  {
    for(i=0;i<max-1;i++)
    {
      if(line[i]=='/' && line[i+1]=='*')
      {
        for(m=i;i<max-1;m++)
        {
          if(line[m]=='*' && line[m+1]=='/')
          {
            i=m+2;
          }
        }
      }
      else
      {
        printf("%s",&line[i]);
      }
    }
  }
return 0;
}

int getline(char s[], int limit)
{
  int i,c;
  for(i=0;i<max-1 && (c=getchar())!=EOF && c!='\n';++i)
    line[i]=c;
  return i;
}
