/*
Trie Data Structure

Time Complexity
  Search - O(n)
  Insert - O(n)
  Delete - O(n)

*/


#include <iostream>
#include <unordered_map>
#include <stdlib.h>
#include <string>
using namespace std;

struct node{
  char data;
  unordered_map<char, struct node*> children;
  bool endOfString;
};

typedef struct node* Node;


Node createNode(char data){
  Node newNode = new node;
  newNode->data = data;
  newNode->children;
  newNode->endOfString = false;
  return newNode;
}



void insert(Node root, char* s){
  if(*s == '\0'){
    root->endOfString = true;
    return;
  }

  unordered_map<char, Node>::iterator it;

  it = root->children.find(*s);
  if(it == root->children.end()){
    Node newNode = createNode(*s);
    root->children[*s] = newNode;
  }

  root = root->children[*s];
  cout<<root->data;
  if(*(s+1) == '\0'){
    root->endOfString = true;
    return;
  }
  insert(root, s+1);
}


bool isPresent(Node root, char* s){
    if(*s == '\0' && root->endOfString) return true;
    else if(*s == '\0') return false;

    unordered_map<char, Node>::iterator it;
    it = root->children.find(*s);
    if(it == root->children.end()) return false;

    return isPresent(root->children[*s], s+1);
}


bool isPrefix(Node root, char* s){
  if(*s == '\0') return true;

  unordered_map<char, Node>::iterator it;
  it = root->children.find(*s);
  if(it == root->children.end()) return false;

  return isPrefix(root->children[*s], s+1);
}


// void pri(Node root){
//   for(unordered_map<char, Node>::iterator it = root->children.begin(); it != root->children.end(); it++)
//     cout<<it->first;
// }


void testcases(Node root){
  insert(root, "abc"); cout<<"\n";
  insert(root, "ab"); cout<<"\n";
  insert(root, "abcd"); cout<<"\n";
  insert(root, "abe"); cout<<"\n";
  insert(root, "bcd"); cout<<"\n";
  cout<<isPresent(root, "bc")<<"\n";
  cout<<isPresent(root, "abc")<<"\n";
  cout<<isPresent(root, "bcd")<<"\n";
  cout<<isPresent(root, "b")<<"\n";


  cout<<isPrefix(root, "bc")<<"\n";
  cout<<isPrefix(root, "abc")<<"\n";
  cout<<isPrefix(root, "bcd")<<"\n";
  cout<<isPrefix(root, "xyz")<<"\n";
}



int main(){
  //Root node has no data
  Node root = createNode('#');
  // testcases(root);
  return 0;
}
