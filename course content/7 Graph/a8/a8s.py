import sys

def kos(n, adj_list):
    visited = [False] * n
    f_stack = []
    r_adj_list = [[] for _ in range(n)]

    def dfs1(v):
        visited[v] = True
        for neighbor in adj_list[v]:
            if not visited[neighbor]:
                dfs1(neighbor)
        f_stack.append(v)
        
        for u in range(n):
            for v in adj_list[u]:
                r_adj_list[v].append(u)
    
    def dfs2(v, component):
        visited[v] = True
        component.append(v)
        for neighbor in r_adj_list[v]:
            if not visited[neighbor]:
                dfs2(neighbor, component)
    
    for i in range(n):
        if not visited[i]:
            dfs1(i)

    visited = [False] * n
    strong = []
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
        
        sccs = kos(n, adj_list)
        print(len(sccs))

if __name__ == "__main__":
    main()