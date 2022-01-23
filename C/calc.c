#include<stdio.h>
#define NUMBER '1','2';

int main()
{
  int c;
  while((c=getchar())!=EOF && c!='\n')
  {
    switch(c){
      case NUMBER:
        printf("Number\n");
        break;
      default:
        printf("Wrong Input\n");
        break;
    }
  }
  return 0;
}
