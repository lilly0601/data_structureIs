graph = {
    1: [0, 1, 0, 0, 1, 0],
    2: [1, 0, 1, 0, 0, 0],
    3: [0, 1, 0, 1, 0, 0],
    4: [0, 0, 1, 0, 0, 1],
    5: [1, 0, 0, 0, 0, 1],
    6: [0, 0, 0, 1, 1, 0]
}
u = 5
v = 6
is_connected = False

value = graph.get(u)
if value [v-1] == 1:
    is_connected = True

print(is_connected)