/*
Quick Sort 

Time Complexity - O(n^2) in the worst case; O(nlogn) when randomized partitioning is performed
Space Complexity - O(log n), since logn is negligible, quick sort can be claimed as In-place sorting algorithm
*/

#include <iostream>
using namespace std;

void swap(int * arr, int x, int y){
    int temp;
    temp = arr[x];
    arr[x] = arr[y];        
    arr[y] = temp;
}


int partition(int* arr, int start, int end){
    int pivotValue = arr[end];
    int pivotIndex = start, temp;

    for(int i = start; i < end; i++){
        if(arr[i] <= pivotValue){
            swap(arr, i, pivotIndex);
            pivotIndex++;
        }
    }

    swap(arr, pivotIndex, end);
    return pivotIndex;
}


void quickSort(int* arr, int start, int end){
    if(start < end){
        // O(n)
        int partitionIndex = partition(arr, start, end);
        quickSort(arr, start, partitionIndex - 1);
        quickSort(arr, partitionIndex + 1, end);
    }
}


int main(){
    int arr[] = {9, 183, 23 , 46, 45, 22, 12, 3};
    quickSort(arr, 0, sizeof(arr) / sizeof(int) - 1);

    for(int i = 0; i < sizeof(arr) / sizeof(int); i++)  cout<<arr[i] << " "; 
    
    return 0;
}