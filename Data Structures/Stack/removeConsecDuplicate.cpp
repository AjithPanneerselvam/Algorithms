/*
Given a string, return the number of length of a resultant string which is made up of characters in the input string, where no adjacent characters are same.

Example:
  Input: abaeeaf
  Output: 3 (abf)
Time Complexity - O(n)
Space Complexity - O(n)
*/

#include <iostream>
#include <stdlib.h>
#include <stack>

using namespace std;

int main() {
    int n, result = 0, i = 0;
    char* s, top;
    stack<char> st;

    cin>>n;
    s = (char *)malloc(sizeof(char));
    cin>>s;

    while(s[i] != '\0'){
        if(!st.empty() && s[i] == st.top()) st.pop();
        else st.push(s[i]);
        i++;
    }

    while(!st.empty()){
        st.pop();
        result++;
    }

    cout<<result;
    return 0;
}
