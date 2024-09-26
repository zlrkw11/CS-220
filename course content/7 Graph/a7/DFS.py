import sys

def dfs(adj_list):
    global visited, S
    visited = [False] * len(adj_list)
    heights = []
    for i in range(len(adj_list)):
        if not visited[i]:
            height = dfs_visit(i, adj_list)
            heights.append(height)
    
    print(' '. join(map(str, heights)))
        
def dfs_visit(start, adj_list):
  
    
    max_height = 0
    S = [(start, 0)]
    while len(S) != 0:
        node, height = S[-1]
        visited[node] = True
        max_height = max(max_height, height)
        POP_STATEMENT = True
        for neighbor in sorted(adj_list[node]):
            if not visited[neighbor]:
                visited[neighbor]= True
                S.append((neighbor, height+1))
                POP_STATEMENT = False
                break
        if POP_STATEMENT and len(S) > 0:
            S.pop(-1)
    return max_height 
    
def main():
     while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break

        adj_list = []
        for _ in range(n):
            neighbors = list(map(int, sys.stdin.readline().strip().split()))
            adj_list.append(neighbors)

        dfs(adj_list)

if __name__ == "__main__":
    main()
