/*
Maximum Length Chain of Pairs
https://www.geeksforgeeks.org/dynamic-programming-set-20-maximum-length-chain-of-pairs/
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion.
Find the longest chain which can be formed from a given set of pairs.

For example, if the given pairs are {{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90} },
then the longest chain that can be formed is of length 3, and the chain is {{5, 24}, {27, 40}, {50, 90}}

Time Complexity - O(n^2)
Space Complexity - O(n)
*/

#include <iostream>
#include <vector>
using namespace std;

struct point{
  int x;
  int y;
};


bool sortFunction(point i, point j){
  return (i.y < j.x);
}


int maxLengthPairs(point* p, int n){
  vector<int> maxLength(n, 1);
  sort(p, p+n, sortFunction);
  int maxLen = -1;

  for(int i = 0; i < n; i++){
    for(int j = 0; j < i; j++){
      if(p[j].y < p[i].x && maxLength[j] + 1 > maxLength[i]){
        maxLength[i] = maxLength[j] + 1;
        if(maxLength[i] > maxLen) maxLen = maxLength[i];
      }
    }
  }
  return maxLen;
}


// void testcases(){
//   int n;
//   cin>>n;
//   point p[n];
//   for(int i = 0; i < n; i++){
//     cin>>p[i].x>>p[i].y;
//   }
//   cout<<maxLengthPairs(p, n);
// }


int main(){
  // testcases();
  return 0;
}
