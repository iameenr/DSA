#include <stdio.h>

int main()
{
  int c,n=0;
  printf("Enter: \n");
  while((c=getchar())!=EOF){
    if(c=='\n')
      ++n;
    printf("Number: %d\n",n);
  }
  return 0;
}

/*me
number 0
number 0
number 1*/
