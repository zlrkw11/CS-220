import sys

def dfs(adj_list, n):
    # Initialize data structures
    color = ['WHITE'] * n
    pred = [None] * n
    seen = [-1] * n
    done = [-1] * n
    heights = [-1] * n  # To store the height of each subtree
    time = [0]  # To track the time

    # Helper function for DFS visit
    def dfsvisit(node):
        nonlocal time
        color[node] = 'GREY'
        seen[node] = time[0]
        time[0] += 1
        stack = [node]
        max_depth = {node: 0}  # Track max depth from this node

        while stack:
            u = stack[-1]
            has_unvisited_child = False

            for v in adj_list[u]:
                if color[v] == 'WHITE':
                    color[v] = 'GREY'
                    pred[v] = u
                    seen[v] = time[0]
                    time[0] += 1
                    stack.append(v)
                    max_depth[v] = max_depth[u] + 1  # Update depth
                    has_unvisited_child = True
                    break

            if not has_unvisited_child:
                stack.pop()
                color[u] = 'BLACK'
                done[u] = time[0]
                heights[u] = max_depth[u]  # Store the max depth (height)
                time[0] += 1

    # Run DFS on all nodes to ensure all trees are visited
    for s in range(n):
        if color[s] == 'WHITE':
            dfsvisit(s)

    return heights

def main():
    while True:
        # Read the number of vertices
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break  # Terminate when a graph of order 0 is encountered

        # Read adjacency lists
        adj_list = []
        for _ in range(n):
            row = list(map(int, sys.stdin.readline().strip().split()))
            adj_list.append(row)

        # Perform DFS and get the heights of trees
        heights = dfs(adj_list, n)

        # Print the height of each tree
        if heights:
            max_tree_height = max(heights)
            print(' '.join(map(str, heights)))
        else:
            print(0)

if __name__ == "__main__":
    main()

