import sys

def m_al():
    while True:
        n = int(sys.stdin.readline().strip())
        if n==0:
            print(n)
            break
        adjacency_list = []

        for i in range(n):
            row = sys.stdin.readline().strip().split()
            neighbors = []
            for j in range(n):
                if row[j] == '1':
                    neighbors.append(j)
            adjacency_list.append(neighbors)

        print(n)
        for neighbors in adjacency_list:
            print(' '.join(map(str, sorted(neighbors))))

if __name__ == "__main__":
    m_al()
        

