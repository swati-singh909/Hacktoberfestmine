// Question is we've to print every possible permutations of given string.
// For ex:-abc
// (a)(b)(c)
// (abc)


// solution:-

#include <bits/stdc++.h>
using namespace std;

bool isPalindrome(string s){
    for(int i=0,j=s.size()-1;i<j;i++,j--){
        if(s[i]!=s[j])  return false;
    }
    return true;
}

void solve(string s,string asf){
    if(s.size()==0){
        cout<<asf<<endl;
        return;
    }
    string f="";
    for(int i=0;i<s.size();i++){
        f+=s[i];
        if(isPalindrome(f)){
            int n=s.size()-1;
            n=n-i;
            string p=s.substr(i+1,n);
            solve(p,asf+"("+f+")");
        }
    }
}

int main() {
    string s;
    cin>>s;
    solve(s,"");
    return 0;
}
