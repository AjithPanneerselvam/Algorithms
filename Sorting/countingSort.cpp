/*
Counting sort - It is a variation of counting sort algorithm writtein in countingSort.py

Time Complexity - O(n)
Space Complexity - O(n) + O(k) 
*/

#include <iostream>
#include <vector>
using namespace std;

vector<int> countingSort(vector<int> &arr, vector<int> &result, int n, int k){
    vector<int> temporaryArr(k+1, 0);

    for(int i = 0; i < arr.size(); i++) temporaryArr[arr[i]] += 1;

    for(int i = 1; i <= k; i++) temporaryArr[i] += temporaryArr[i-1];

    for(int i = 0; i < n; i++){
        result[temporaryArr[arr[i]] - 1] = arr[i];
        temporaryArr[arr[i]] -= 1;
    }

    return result;
}

int main(){
    int n, k;
    cin>>n>>k;
    vector<int> arr(n);
    vector<int> result(n);

    for(int i = 0; i < n; i++)  cin>>arr[i];

    countingSort(arr, result, n, k);

    for(int i = 0; i < n; i++) cout<<result[i] << " ";
    
    return 0;
}