#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // Your code goes here...
    long T,N,n1,n2;
    cin>>T;
    while(T--)
    {
        cin>>N;
        int d =(int)log2(N) + 1;
        n1 = (int)pow(2,d-1)-1;
        n2 = n1 xor N;
        cout<<n1*n2<<"\n";
    }
return 0;
}