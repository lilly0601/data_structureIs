# 7.	Проверка наличия параллельных рёбер.
graph = {
    1: [0, 1, 1],   # 1 → 1 появляется дважды → параллельное ребро
    2: [1, 0, 0],
    3: [1, 0, 0]
}
def has_parallel_edges(graph):
    for u in graph:
        neighbors = graph[u]
        seen = set()

        for v in neighbors:
            if v in seen:   # дубликат → параллельное ребро
                return True
            seen.add(v)

    return False

print("Есть параллельные рёбра?", has_parallel_edges(graph))