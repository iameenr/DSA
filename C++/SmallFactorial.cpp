#include <iostream>

using namespace std;

int factorialDigits[200] = {0};
int noOfDigits;

void factorialByCarryMethod(int num){
    int i,j, multiple, carry;
    factorialDigits[0] = 1;
    noOfDigits = 1;
    
    for(i=2; i<=num; i++){
        carry=0;
        for(j=0; j<noOfDigits; j++){
        multiple = (i*factorialDigits[j]) + carry;
        factorialDigits[j] = multiple%10;                //Remainder
        carry = multiple/10;                            //Carry
        }
        while(carry){
            factorialDigits[noOfDigits] = carry%10;
            carry= carry/10;
            noOfDigits++;
        }
    }
    return;
}

void printResult(){
    int i;
    for(i=noOfDigits-1; i>=0; i--)
        cout<<factorialDigits[i];
    cout<<'\n';
    
}

void reInitializeZeroes(){
    int i;
    for(i=0; i<200; i++)
        factorialDigits[i]=0;
    return;
}

int main()
{
    ios_base::sync_with_stdio(false);
    
    //Reading Input
    int numOfInputs;
    cin>>numOfInputs;
    int inputs[numOfInputs], i;
    for(i=0; i<numOfInputs; i++)
        cin>>inputs[i];

    //Solution
    for(i=0; i<numOfInputs; i++){
        if(inputs[i] != 0 || inputs[i] != 1){
            factorialByCarryMethod(inputs[i]);
            printResult();
            reInitializeZeroes();
        }
        else
            cout<<1<<'\n';
    }

    return 0;
}