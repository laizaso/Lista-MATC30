import numpy as np

def resolver_labirinto(n, m, k, maze, tunnels):
    tunnel_map = {}
    for i1, j1, i2, j2 in tunnels:
        tunnel_map[(i1-1, j1-1)] = (i2-1, j2-1) 
        tunnel_map[(i2-1, j2-1)] = (i1-1, j1-1)

    start = None
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'A':
                start = (i, j)
                break
        if start:
            break

    index = {}
    idx = 0
    for i in range(n):
        for j in range(m):
            if maze[i][j] != '#':
                index[(i, j)] = idx
                idx += 1

    N = len(index)
    if N == 0:
        return 0.0

    A = np.zeros((N, N))
    B = np.zeros(N)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for (i, j), idx_ij in index.items():
        cell_type = maze[i][j]

        if cell_type == '*':  
            A[idx_ij][idx_ij] = 1
            B[idx_ij] = 0
        elif cell_type == '%':  
            A[idx_ij][idx_ij] = 1
            B[idx_ij] = 1
        else:
            neighbors = []
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != '#':
                    # Verifica se é entrada de túnel
                    if (ni, nj) in tunnel_map:
                        ni, nj = tunnel_map[(ni, nj)]
                    neighbors.append((ni, nj))

            if not neighbors:
                A[idx_ij][idx_ij] = 1
                B[idx_ij] = 0
            else:
                A[idx_ij][idx_ij] = 1
                for ni, nj in neighbors:
                    if (ni, nj) in index:  
                        A[idx_ij][index[(ni, nj)]] -= 1 / len(neighbors)

    try:
        probs = np.linalg.solve(A, B)
        return float(probs[index[start]])
    except np.linalg.LinAlgError:
        return 0.0

def main():
    n, m, k = 3, 6, 1
    maze = [
        "###*OO",
        "O#OA%O",
        "###*OO"
    ]
    tunnels = [(2, 3, 2, 1)]  
    resultado = resolver_labirinto(n, m, k, maze, tunnels)
    print("Probabilidade de fuga: {0:.4f}".format(resultado))

if __name__ == '__main__':
    main()