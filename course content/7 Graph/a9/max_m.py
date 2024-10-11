import sys
from collections import deque

# BFS to check for augmenting paths in the Hopcroft-Karp algorithm
def bfs(graph, pair_u, pair_v, dist, u_size):
    queue = deque()
    
    # Enqueue all free vertices in U
    for u in range(u_size):
        if pair_u[u] == -1:  # Free vertex
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float('inf')

    dist[-1] = float('inf')  # NIL vertex

    while queue:
        u = queue.popleft()
        if dist[u] < dist[-1]:  # If there is still an augmenting path
            for v in graph[u]:
                if pair_v[v] == -1 or dist[pair_v[v]] == float('inf'):
                    dist[pair_v[v]] = dist[u] + 1
                    queue.append(pair_v[v])
    
    return dist[-1] != float('inf')

# DFS to perform the augmenting path search in Hopcroft-Karp
def dfs(graph, u, pair_u, pair_v, dist):
    if u != -1:
        for v in graph[u]:
            if pair_v[v] == -1 or dist[pair_v[v]] == dist[u] + 1:
                if dfs(graph, pair_v[v], pair_u, pair_v, dist):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
        dist[u] = float('inf')
        return False
    return True

# Hopcroft-Karp algorithm to find the maximum matching
def hopcroft_karp(graph, u_size, v_size):
    pair_u = [-1] * u_size  # -1 means unmatched
    pair_v = [-1] * v_size  # Similarly for vertices in V
    dist = [-1] * (u_size + 1)  # NIL is at index u_size

    matching = 0

    while bfs(graph, pair_u, pair_v, dist, u_size):
        for u in range(u_size):
            if pair_u[u] == -1:  # Free vertex in U
                if dfs(graph, u, pair_u, pair_v, dist):
                    matching += 1

    return matching

def main():
    while True:
        n = int(sys.stdin.readline().strip())  # Read number of nodes
        if n == 0:
            break
        
        adj_list = []
        for _ in range(n):
            neighbors = list(map(int, sys.stdin.readline().strip().split()))
            adj_list.append(neighbors)

        # We assume the graph is bipartite and partitioned into two sets U and V
        u_size = n  # Let's assume all nodes are in set U
        v_size = n  # Corresponding number of nodes in set V (adjust as needed)

        # Find the maximum matching using the Hopcroft-Karp algorithm
        matching_size = hopcroft_karp(adj_list, u_size, v_size) // 2
        print(matching_size)

if __name__ == "__main__":
    main()
