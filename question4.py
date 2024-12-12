import heapq

def prim_mst(V, adj):
    total_weight = 0
    visited = [False] * V
    min_heap = [(0, 0)]  # (weight, vertex)
    
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        total_weight += weight
        
        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
    
    return total_weight

def main():
    # Read the number of vertices and edges
    V, E = map(int, input("Enter number of vertices and edges (V E): ").split())
    
    # Create an adjacency list
    adj = [[] for _ in range(V)]
    
    print("Enter edges (u v weight) for each edge:")
    for _ in range(E):
        u, v, weight = map(int, input().split())
        adj[u].append((v, weight))
        adj[v].append((u, weight))  # Since the graph is undirected
    
    # Calculate the weight of the Minimum Spanning Tree
    mst_weight = prim_mst(V, adj)
    print("The sum of the weights of the edges in the Minimum Spanning Tree is:", mst_weight)

if __name__ == "__main__":
    main()