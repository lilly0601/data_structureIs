def find_components_after_removal(adj_list, V_count, v_to_remove):
    
    new_vertices = set(range(1, V_count + 1)) - {v_to_remove}
    
    visited = {v: False for v in new_vertices}
    component_count = 0

    def dfs(u):
        visited[u] = True
        for w in adj_list.get(u, []): 
            if w != v_to_remove and not visited.get(w, True):
                dfs(w)

    for v in sorted(list(new_vertices)):
        if not visited[v]:
            component_count += 1
            dfs(v)
            
    return component_count

V_TOTAL = 5
GRAPH = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2, 4],
    4: [3, 5],
    5: [4]
}

V_TO_REMOVE_1 = 5
count_1 = find_components_after_removal(GRAPH, V_TOTAL, V_TO_REMOVE_1)
print(f"5-ші төбені алып тастағаннан кейін (1-2-3-4 қалды): {count_1} компонент") 

V_TO_REMOVE_2 = 3
count_2 = find_components_after_removal(GRAPH, V_TOTAL, V_TO_REMOVE_2)
print(f"3-ші төбені алып тастағаннан кейін ({'{1, 2}'}  және {'{4, 5}'} қалды): {count_2} компонент")