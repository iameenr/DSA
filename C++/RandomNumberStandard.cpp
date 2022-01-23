#include<iostream>
#include<random>

using namespace std;

int main()
{
    int a,b, RandomNumber;
    cin>>a>>b;

    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> distribute(a,b);
    RandomNumber = distribute(gen);

    cout<<RandomNumber;

}