def dfs_traversal(adj):
    """
    Performs a Depth First Traversal (DFS) on a given graph represented by an adjacency list.

    Args:
        adj (list): Adjacency list representing the graph.

    Returns:
        list: A list containing the DFS traversal of the graph.
    """
    visited = set()
    traversal_order = []

    def dfs(vertex):
        """
        Recursive function to perform DFS traversal.

        Args:
            vertex (int): Current vertex being visited.
        """
        visited.add(vertex)
        traversal_order.append(vertex)

        for neighbor in adj[vertex]:
            if neighbor not in visited:
                dfs(neighbor)

    # Start DFS traversal from vertex 0
    dfs(0)

    return traversal_order


def main():
    # Input the number of vertices in the graph
    num_vertices = int(input("Enter the number of vertices in the graph: "))

    # Input the adjacency list
    adj = []
    for i in range(num_vertices):
        neighbors = list(map(int, input(f"Enter the neighbors of vertex {i} (space-separated): ").split()))
        adj.append(neighbors)

    # Perform DFS traversal
    traversal_order = dfs_traversal(adj)

    # Print the DFS traversal order
    print("DFS Traversal Order:", traversal_order)


if __name__ == "__main__":
    main()