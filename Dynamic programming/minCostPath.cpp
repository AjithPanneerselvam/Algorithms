/*
Minimum Cost Path
https://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/

Time Complexity - O(n^2)
Space Complexity - O(n ^ 2)
*/

#include<iostream>
#include<stdlib.h>
using namespace std;

int findMinimum(int x, int y, int z){
  if(x < y){
    return x < z? x: z;
  }
  return y < z? y: z;
}


int minimumCostPath(int** costPath, int** dynArray, int n){
  dynArray[0][0] = costPath[0][0];

  // Fill the fisrt row
  for(int j = 1; j < n; j++)
    dynArray[0][j] = dynArray[0][j-1] + costPath[0][j];

  // Fill the first column
  for(int i = 0; i < n; i++)
    dynArray[i][0] = dynArray[i-1][0] + costPath[i][0];

  for(int i = 1; i < n; i++){
    for(int j = 1; j < n; j++){
      dynArray[i][j] = costPath[i][j] + findMinimum(dynArray[i][j-1], dynArray[i-1][j-1], dynArray[i-1][j]);
    }
  }
  return costPath[n-1][n-1];
}


int main(){
  int n;
  cin>>n;

  // Create a 2D Array
  int** costPath = (int **) malloc(sizeof(n * (int *)));
  int** dynArray = new n * (int*);
  for(int i = 0; i < n; i++){
    costPath[i] = new n * (int);
    dynArray[i] = new n * (int)
  }

//Enter the cost of the Path
  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      cin>>costPath[i][j];
    }
  }

  cout<<minimumCostPath(costPath, dynArray, n);

  return 0;
}
