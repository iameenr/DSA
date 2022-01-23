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
    for(i=0;i<max-1 && line[i]!='\0';i++)
      printf("%s",&line[i]);
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
