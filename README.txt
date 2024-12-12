# hw_1123552
Author: Amylea
Submission date: 2024.11.28
Github link: https://github.com/Amyleea05/hw3_1123552

IMPORTANT NOTE!
Input commands used in all the codes. Therefore, in order to get the output, you need to manually provide all the inputs. You can use examples on the documents or the example inputs and outputs below (that different from documents). 

QUESTION 1:
Given an undirected graph with V nodes and E edges, create and return an adjacency list of the graph. 0-based indexing is followed everywhere.
Input example:
Enter number of vertices (V): 5
Enter number of edges (E): 7
Enter the edges in the format 'u v' (one per line):
0 1
0 4
4 1
4 3 
1 3
1 2
3 2
Output: 
Adjacency List:
0: [1, 4]
1: [0, 4, 3, 2]
2: [1, 3]
3: [4, 1, 2]
4: [0, 1, 3]

QUESTION 2:
Given a connected undirected graph represented by an adjacency list adj, which is a vector of vectors where each adj[i] represents the list of vertices connected to vertex i. Perform a Breadth First Traversal (BFS) starting from vertex 0, visiting vertices from left to right according to the adjacency list, and return a list containing the BFS traversal of the graph.
Input example:

Output:

QUESTION 3:
Given a connected undirected graph represented by an adjacency list adj, which is a vector of vectors where each adj[i] represents the list of vertices connected to vertex i. Perform a Depth First Traversal (DFS) starting from vertex 0, visiting vertices from left to right as per the adjacency list, and return a list containing the DFS traversal of the graph.
Input example:

Output:

QUESTION 4:
Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is represented by an adjacency list, where each element adj[i] is a vector containing vector of integers. Each vector represents an edge, with the first integer denoting the endpoint of the edge and the second integer denoting the weight of the edge.
Input example:
Enter number of vertices and edges (V E): 3 3
Enter edges (u v weight) for each edge:
0 1 5
1 2 3
0 2 1
Output:
The sum of the weights of the edges in the Minimum Spanning Tree is: 4
