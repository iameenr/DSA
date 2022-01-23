#include<stdio.h>
#define maxline 100

int getline(char line[],int maxline);
int copy(char from[],to[]);

main()
{
  char line[maxline],longestline[maxline];
  int max,len;

  max=0;
  while((len=getline(line,maxline))>0)
  {
    if(len>max){
      max=len;
      copy(line,longest);
    }
  }
  if(max>0){
    printf("%s",longest);
  }
  return 0;
}
