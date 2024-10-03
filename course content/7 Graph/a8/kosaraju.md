## Kosaraju's Algorithm

### Run DFS first, then back again in reversed graph
The nodes which are strongly connected are the only ones which will be reached.

When a node finishes in the first DFS, it means we explored all its reachable nodes. In the reversed graph, processing from the last finished node ensures that we capture all nodes that are mutually reachable (i.e., belong to the same SCC).