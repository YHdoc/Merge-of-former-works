#include<iostream>
using namespace std;


int sum(int a, int b){
    if (a > b) return 0;
    else if (a == b) return a;
    int m = (a+b)/2;
    return sum(a,m)+sum(m+1,b);
}

int main()
{
    int a,b;
    cin >> a >> b;
    cout<<sum(a,b);
    return 0;
}