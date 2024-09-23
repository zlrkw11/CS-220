import sys


def dfs():
    color = ['WHITE'] * n
    pred = [None] * n
    seen = [] * n
    done = [] * n
    heights = [-1] * n
    time = [0]
    
def main():
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            return 

        arr = []
        for _ in range(n):
            row = list(map(int, sys.stdin.readline().strip().split()))
            arr.append(row)

        heights = dfs(arr, n)

        if heights:
            
    
