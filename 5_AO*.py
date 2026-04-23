### Implement AO* search algorithm to find the optimal path in given problem space.


graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],  
    'B': [[('E', 1)], [('F', 1)]],            
    'C': [[('G', 1)]],                        
    'D': [[('H', 1)]],                        
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

heuristic = {
    'A': 10,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0
}

solution_graph = {}

def ao_star(node):
    
    if not graph[node]:
        return heuristic[node]

    min_cost = float('inf')
    best_path = None

    for path in graph[node]:
        cost = 0
        sub_nodes = []

        for (child, weight) in path:
            cost += weight + ao_star(child)
            sub_nodes.append(child)

        if cost < min_cost:
            min_cost = cost
            best_path = sub_nodes
    
    heuristic[node] = min_cost
    
    solution_graph[node] = best_path

    return heuristic[node]

start_node = 'A'
ao_star(start_node)


print("Optimal Cost:", heuristic[start_node])
print("Optimal Solution Graph:")

def print_solution(node):
    if node not in solution_graph:
        return
    print(f"{node} -> {solution_graph[node]}")
    for child in solution_graph[node]:
        print_solution(child)

print_solution(start_node)
