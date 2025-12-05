# 9нұсқа
graph = {
    1: [1, 2],
    2: [3],
    3: [],
    4: [2],
    5: []
}

def adjlist_to_matrix(adj_list):
    n = len(adj_list)
    matrix = [[0]*n for _ in range(n)]
    for i in adj_list:
        for j in adj_list[i]:
            matrix[i-1][j-1] = 1
    return matrix

if __name__ == "__main__":
    adjacency_matrix = adjlist_to_matrix(graph)
    
    for row in adjacency_matrix:
        print(row)
