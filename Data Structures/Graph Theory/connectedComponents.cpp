/*
To find the number of connected graphs using depth first search
*/

#include <iostream>
#include <vector>
using namespace std;

bool visited[100];
vector<int> adjaceny_list[100];


void find_connected(int source){
    visited[source] = true;
    for(int i = 0; i < adjaceny_list[source].size(); i++){
        if(visited[adjaceny_list[source][i]] == false)
            find_connected(adjaceny_list[source][i]);
    }
}


int main(){
    int i, j, nodes, edges, vertices1, vertices2, connected_components = 0, numNodes;

    cin >> numNodes;

    // It is assumed that vertex label are indexed from 1 to number of nodes
    for(i = 1; i <= numNodes; i++)
        visited[i] = false;

    cin >> edges;

    for(i = 0 ; i < edges; i++){
        cin >> vertices1 >> vertices2;
        adjaceny_list[vertices1].push_back(vertices2);
        adjaceny_list[vertices2].push_back(vertices1);
    }

    for(i = 1; i <= numNodes; i++){
        if(visited[i] == false){
            find_connected(i);
            connected_components++;
        }
    }

    cout << "\nNumber of connected graphs are " << connected_components <<"\n";
    return 0;
}
