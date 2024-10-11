import sys
from collections import deque

def is_bipartite(adj_list, n):
    color = [-1] * n 

    for start in range(n):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()

                for neighbor in adj_list[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
    return True

def main():
    while True:
        n = int(sys.stdin.readline().strip())  # Read number of nodes
        if n == 0:
            break
        
        adj_list = []
        for _ in range(n):
            neighbors = list(map(int, sys.stdin.readline().strip().split()))
            adj_list.append(neighbors)

        print(is_bipartite(adj_list, n))

if __name__ == "__main__":
    main()