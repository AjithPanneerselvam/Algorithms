/*
Trie Data Structure

Time Complexity
  Search - O(n)
  Insert - O(n)
  Delete - O(n)
where n is the length of the string

Space Complexity - (W * l), where W is the number of words and l is the average length of the words
*/


#include <iostream>
#include <unordered_map>
#include <stdlib.h>
#include <string>
using namespace std;

struct node{
  char data;
  unordered_map<char, struct node*> children;
  int frequency;
  bool endOfString;
};

typedef struct node* Node;


Node createNode(char data){
  Node newNode = new node;
  newNode->data = data;
  newNode->children;
  newNode->frequency = 0;
  newNode->endOfString = false;
  return newNode;
}



void insert(Node root, char* s){
  root->frequency += 1;
  cout<<root->data;
  
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


bool del(Node root, char* s){
  if(*s == '\0') {
    if(root->endOfString){
      root->endOfString = false;
      root->frequency -= 1;
      return 1;
    }
    return 0;
  }
  
  unordered_map<char, Node>::iterator it;
  it = root->children.find(*s);
  if(it == root->children.end()) return 0; 
  
  if(del(root->children[*s], s+1)){
    root->frequency -= 1;
    if(root->children.find(*s) != root->children.end() && root->children[*s]->frequency == 0){
      Node tempNode = root->children[*s];
      root->children.erase(*s);
      delete tempNode;
    }
    return 1;
  }

  return 0;
}


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
  
  cout<<"Delete status - " << del(root, "abc")<<"\n";  
  cout<<"Is present? " <<isPresent(root, "abc")<<"\n";
  cout<<"Delete status - " << del(root, "abc")<<"\n";
  cout<<"Is present? " << isPresent(root, "abc")<<"\n";
  cout<<"Delete status - " << del(root, "abcd")<<"\n";
  cout<<"Is present? " << isPresent(root, "abcd")<<"\n";

}



int main(){
  //Root node has no data
  Node root = createNode('#');
  testcases(root);
  return 0;
}
