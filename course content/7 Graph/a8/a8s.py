import sys

def kosaraju_scc(n, adj_list):
    visited = [False] * n
    f_stack = []
    r_adj_list = [[] for _ in range(n)]

    def dfs1(v):
        stack = [v]
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                for neighbor in adj_list[current]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
                f_stack.append(current)  # Append after visiting all neighbors

    # Build the transposed graph
    for u in range(n):
        for v in adj_list[u]:
            r_adj_list[v].append(u)

    # First DFS to get the finishing order
    for i in range(n):
        if not visited[i]:
            dfs1(i)

    # Reset visited for the second DFS
    visited = [False] * n
    strong = []

    def dfs2(v, component):
        stack = [v]
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                component.append(current)
                # Explore the transposed graph
                for neighbor in r_adj_list[current]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

    # Second DFS on transposed graph based on finishing order
    while f_stack:
        node = f_stack.pop()
        if not visited[node]:
            component = []
            dfs2(node, component)
            strong.append(component)
    
    return strong

def main():
    while True:
        n = int(sys.stdin.readline().strip())  # Read number of nodes
        if n == 0:
            break
        
        adj_list = []
        for _ in range(n):
            neighbors = list(map(int, sys.stdin.readline().strip().split()))
            adj_list.append(neighbors)
        
        sccs = kosaraju_scc(n, adj_list)
        print(len(sccs))  # Output the number of strongly connected components

if __name__ == "__main__":
    main()
