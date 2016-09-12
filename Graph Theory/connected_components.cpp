/*
To find the number of connected graphs using depth first search
*/

#include <iostream>
#include <vector>
using namespace std;

bool visited[11];
vector <int > adjaceny_list[11];

void find_connected(int source)
{
    visited[source] = true;
    for(int i = 0; i < adjaceny_list[source].size(); i++ )
    {
        if(visited[adjaceny_list[source][i]] == false)
            find_connected(adjaceny_list[source][i]);
    }
}

int main()
{
    int i,j,nodes,edges,vertices1,vertices2,connected_components=0;

    for(i = 1 ; i <= 10; i++)                    // Marking all the nodes as unvisited
    {
        visited[i] = false;
    }

    cin >> nodes >> edges;
    for(i = 0 ;i<edges;i++)                     // Creating adjaceny_list
    {
        cin >> vertices1 >> vertices2;
        adjaceny_list[vertices1].push_back(vertices2);
        adjaceny_list[vertices2].push_back(vertices1);
    }

/*
    for (i = 1; i <= nodes; i++)                                    // To display the adjacency list
    {
        cout<<"\nThe nodes connected to" << i <<" are.. ";
        for (j = 0; j < adjaceny_list[i].size(); j++)
        {
            cout<<adjaceny_list[i][j]<<" ";
        }
    }
*/
    for(i = 1; i <= nodes; i++)
    {
        if(visited[i] == false)
        {
            find_connected(i);
            connected_components++;
        }
    }

    cout << "\nNumber of connected graphs are " << connected_components;

    return 0;
}
