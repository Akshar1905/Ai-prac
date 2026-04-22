import heapq

def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))  # (f(n), node)

    came_from = {}
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    f_cost = {node: float('inf') for node in graph}
    f_cost[start] = heuristic[start]

    visited_order = []

    while open_list:
        current = heapq.heappop(open_list)[1]
        visited_order.append(current)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return visited_order, path

        for neighbor, cost in graph[current]:
            tentative_g = g_cost[current] + cost

            if tentative_g < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = tentative_g
                f_cost[neighbor] = tentative_g + heuristic[neighbor]

                heapq.heappush(open_list, (f_cost[neighbor], neighbor))

    return visited_order, None




graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'F'

visited, path = a_star(graph, heuristic, start, goal)

print("Visited Order:", visited)
print("Optimal Path:", path)