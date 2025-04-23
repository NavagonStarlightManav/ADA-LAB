def prims_algorithm(num_nodes, cost_matrix):
    INF = float('inf')


    nearest = [INF] * num_nodes


    mst_edges = []


    total_mst_cost = 0


    start_node = end_node = -1
    min_cost = INF
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if cost_matrix[i][j] < min_cost:
                min_cost = cost_matrix[i][j]
                start_node, end_node = i, j


    mst_edges.append((start_node, end_node))
    total_mst_cost += min_cost


    for i in range(num_nodes):
        if cost_matrix[i][start_node] < cost_matrix[i][end_node]:
            nearest[i] = start_node
        else:
            nearest[i] = end_node


    nearest[start_node] = nearest[end_node] = -1


    for _ in range(num_nodes - 2):
        next_node = -1
        min_edge_cost = INF


        for i in range(num_nodes):
            if nearest[i] != -1 and cost_matrix[i][nearest[i]] < min_edge_cost:
                min_edge_cost = cost_matrix[i][nearest[i]]
                next_node = i


        mst_edges.append((next_node, nearest[next_node]))
        total_mst_cost += min_edge_cost


        nearest[next_node] = -1

        # Update nearest nodes if this new one offers a better connection
        for i in range(num_nodes):
            if nearest[i] != -1 and cost_matrix[i][next_node] < cost_matrix[i][nearest[i]]:
                nearest[i] = next_node


    print("Minimum Spanning Tree edges:")
    for u, v in mst_edges:
        print(f"Edge from Node {u} to Node {v}")
    print("Total Cost of MST:", total_mst_cost)

INF = float('inf')
graph = [
    [INF, 2,   INF, 6,   INF],
    [2,   INF, 3,   8,   5],
    [INF, 3,   INF, INF, 7],
    [6,   8,   INF, INF, 9],
    [INF, 5,   7,   9,   INF]
]

prims_algorithm(num_nodes=5, cost_matrix=graph)

