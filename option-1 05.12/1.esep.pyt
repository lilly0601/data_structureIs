from collections import deque
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def bfs(graph, start):
    visited = set()
    q = deque([start])
    order = []
    prime_count = 0
    while q:
        v = q.popleft()
        if v  in visited:
            continue

        visited.add(v)
        order.append(v)

        if is_prime(v):
            prime_count += 1

        for u in graph[v]:
            if u not in visited:
                q.append(u)

    return order, prime_count


graph = {
    1: [2, 3],
    2: [4],
    3: [4, 5],
    4: [6],
    5: [6,7],
    6: [],
    7: []
}
order, primes = bfs(graph, 1)

print("BFS Order:", order)
print("Number of simple vertices:", primes)