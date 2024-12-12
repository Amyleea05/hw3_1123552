def create_adjacency_list(V, E, edges):
    # Initialize the adjacency list
    adjacency_list = [[] for _ in range(V)]
    
    # Populate the adjacency list
    for edge in edges:
        u, v = edge
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    
    return adjacency_list

# Function to take input from the user
def main():
    # Input number of vertices and edges
    V = int(input("Enter number of vertices (V): "))
    E = int(input("Enter number of edges (E): "))
    
    edges = []
    print("Enter the edges in the format 'u v' (one per line):")
    for _ in range(E):
        edge = list(map(int, input().split()))
        edges.append(edge)

    # Calculate the adjacency list
    adjacency_list = create_adjacency_list(V, E, edges)
    
    # Print the adjacency list
    print("Adjacency List:")
    for index, neighbors in enumerate(adjacency_list):
        print(f"{index}: {neighbors}")

if __name__ == "__main__":
    main()
    