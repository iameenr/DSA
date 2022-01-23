/*
Bismillah.
Generating random numbers using the inbuilt function, people say this method is not recommended.

Because it is not uniform.
*/


#include<iostream>
#include<Random>
#include<Time>

int main
{
    //generating a random number in range a to b
    int a,b, RandomNumber;
    cin>>a>>b;

    srand(time(0));
    int Range = (b - a) +1;
    RandomNumber = (rand()%range) + min; //Inlcusive of a and b

    cout<<RandomNumber;

}

