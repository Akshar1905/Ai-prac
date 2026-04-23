### Implement the Minimax algorithm with Alpha-Beta pruning for a game-playing scenario.



def minimax(depth, node_index, is_max, values, alpha, beta, max_depth):
    

    if depth == max_depth:
        return values[node_index]

    if is_max:
        best = float('-inf')

        for i in range(2):  
            val = minimax(depth + 1, node_index * 2 + i,
                          False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)

    
            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2): 
            val = minimax(depth + 1, node_index * 2 + i,
                          True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)

            
            if beta <= alpha:
                break

        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

max_depth = 3  

result = minimax(0, 0, True, values, float('-inf'), float('inf'), max_depth)

print("Optimal value (best move for maximizer):", result)


###🔹 Aim
To implement Minimax algorithm with Alpha-Beta pruning.
🔹 Theory
Minimax is used in game playing where:
Maximizer tries to maximize score
Minimizer tries to minimize score
Alpha-Beta pruning reduces unnecessary calculations.
🔹 Algorithm
Generate game tree
Apply minimax recursively
Use alpha and beta values
Prune branches when possible
🔹 Explanation of Code
Recursive function explores game tree
alpha = best value for maximizer
beta = best value for minimizer
Pruning occurs when beta ≤ alpha
🔹 Conclusion
Alpha-Beta pruning improves efficiency without affecting result.
