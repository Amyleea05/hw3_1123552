from collections import deque

def bfs_traversal(adj):
    visited = set()
    bfs_output = []
    queue = deque([0])  # Start BFS from vertex 0
    visited.add(0)
    
    while queue:
        current = queue.popleft()
        bfs_output.append(current)
        
        # Traverse the neighbors in the order they appear in the adjacency list
        for neighbor in adj[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return bfs_output

# Input: Read the adjacency list
def input_adjacency_list():
    n = int(input("Enter the number of vertices: "))
    adj = []
    for i in range(n):
        # Read the neighbors for vertex i
        neighbors = list(map(int, input(f"Enter the neighbors of vertex {i} (space-separated): ").split()))
        adj.append(neighbors)
    return adj

# Main function to execute the BFS
if __name__ == "__main__":
    adj = input_adjacency_list()
    result = bfs_traversal(adj)
    print("BFS Traversal Output:", result)
    