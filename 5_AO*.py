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


###🔹 Aim
To implement AO algorithm for AND-OR graph*.
🔹 Theory
AO* is used when a problem can be broken into subproblems.
It works on AND-OR graphs:
AND node → all children must be solved
OR node → choose one best child
🔹 Algorithm
Start from root node
Expand nodes
Calculate cost recursively
Choose minimum cost path
🔹 Explanation of Code
Graph contains multiple paths (AND-OR structure)
Recursive function calculates cost
Best path is stored in solution_graph
🔹 Conclusion
AO* is useful for complex decision-making problems involving subgoals.
