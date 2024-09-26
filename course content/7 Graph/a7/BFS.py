import sys

def bfs(adj_list):
    global visited, S
    visited = [False] * len(adj_list)
    heights = []
    for i in range(len(adj_list)):
        if not visited[i]:
            height = bfs_visit(i, adj_list)
            heights.append(height)
    
    print(' '. join(map(str, heights)))
        
def bfs_visit(start, adj_list):
  
    
    max_height = 0
    S = [(start, 0)]
    while len(S) != 0:
        node, height = S[0]
        visited[node] = True
        max_height = max(max_height, height)

        for neighbor in sorted(adj_list[node]):
            if not visited[neighbor]:
                visited[neighbor]= True
                S.append((neighbor, height+1))
                
        S.pop(0)
           
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

        bfs(adj_list)

if __name__ == "__main__":
    main()
