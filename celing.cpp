#include <bits/stdc++.h>
using namespace std;

int ceiling(int arr[], int n, int target)
{
    int s = 0;
    int e = n - 1;
    while (s <= e)
    {
        if(target>arr[n-1]){
            return -1;
        }
        int mid = s + (e - s) / 2;
        if (arr[mid] == target)
        {
            return arr[mid];
        }
        else if(target>arr[mid]){
            s = mid + 1;
        }
        else{
            e = mid - 1;
        }
    }
    return arr[s];
}

    int main()
    {
        int arr[]={2,3,5,9,14,16,18};
        int n=7;
        cout<<ceiling(arr,n,0);
        return 0;
    }