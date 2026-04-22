from collections import deque


def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])  
    traversal = []

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.add(node)
            traversal.append(node)

            if node == goal:
                return traversal, path

            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return traversal, None



def dfs(graph, start, goal):
    visited = set()
    stack = [[start]]  
    traversal = []

    while stack:
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            visited.add(node)
            traversal.append(node)

            if node == goal:
                return traversal, path

            for neighbor in reversed(graph[node]):  
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    return traversal, None



graph = {}
n = int(input("Enter number of nodes: "))

print("Enter adjacency list (node followed by neighbors):")
for _ in range(n):
    node, *neighbors = input().split()
    graph[node] = neighbors

start = input("Enter initial state: ")
goal = input("Enter goal state: ")

bfs_traversal, bfs_path = bfs(graph, start, goal)

dfs_traversal, dfs_path = dfs(graph, start, goal)

print("\n--- BFS Result ---")
print("Traversal Order:", bfs_traversal)
print("Solution Path:", bfs_path if bfs_path else "No path found")

print("\n--- DFS Result ---")
print("Traversal Order:", dfs_traversal)
print("Solution Path:", dfs_path if dfs_path else "No path found")