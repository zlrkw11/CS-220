import sys

def dfs(node, visited, adj_list):
    stack = [node]
    while stack:
        current = stack.pop()
        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

def count_weakly_connected_components(n, adj_list):
    undirected_adj_list = [[] for _ in range(n)]
    
    for u in range(n):
        for v in adj_list[u]:
            undirected_adj_list[u].append(v)
            undirected_adj_list[v].append(u)
    
    visited = [False] * n
    count = 0
    
    for node in range(n):
        if not visited[node]:
            visited[node] = True
            dfs(node, visited, undirected_adj_list)
            count += 1  
    
    return count

def main():
    while True:
        n = int(sys.stdin.readline().strip())  # Read number of nodes
        if n == 0:
            break

        adj_list = []
        for _ in range(n):
            neighbors = list(map(int, sys.stdin.readline().strip().split()))
            adj_list.append(neighbors)

        # Output the number of weakly connected components
        print(count_weakly_connected_components(n, adj_list))

if __name__ == "__main__":
    main()
