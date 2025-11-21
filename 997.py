from collections import deque

n = 3
trust = [[1,3],[2,3],[3,1]]

queue = deque(trust)

in_degree = [0] * (n + 1)
out_degree = [0] * (n +1)

# print(in_degree)
# print(out_degree)

while queue:
    a, b = queue.popleft()
    out_degree[a] += 1
    in_degree[b] += 1 

judge = -1
i = 1
while i <= n:
    if in_degree[i] == n - 1 and out_degree[i] == 0:
        judge = i
        break
    i += 1

print(judge)