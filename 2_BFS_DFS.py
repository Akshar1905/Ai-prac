### Write a program to demonstrate state space search using Breadth First Search (BFS) 
# and Depth First Search (DFS) in Artificial Intelligence. 
# The program should accept a graph, initial state, and goal state as input, p
# erform BFS and DFS traversals, and display the traversal order along with the solution path for both algorithms.

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



///🔹 Aim
To implement Breadth First Search (BFS) and Depth First Search (DFS) for state space search and find traversal order and solution path.
🔹 Theory
State space search is a method used in Artificial Intelligence to explore all possible states to reach a goal.
BFS (Breadth First Search) explores nodes level by level using a queue. It always finds the shortest path in an unweighted graph.
DFS (Depth First Search) explores nodes deeply using a stack. It is memory efficient but may not give the optimal solution.
🔹 Algorithm
BFS Steps:
Start from initial node
Add it to queue
Visit nodes level-wise
Stop when goal is found
DFS Steps:
Start from initial node
Push into stack
Explore deeply
Backtrack if needed
🔹 Explanation of Code
Graph is taken as input using adjacency list
BFS uses queue to explore nodes
DFS uses stack for depth exploration
Traversal order and solution path are printed
🔹 Conclusion
BFS guarantees shortest path, while DFS is faster but not always optimal.
