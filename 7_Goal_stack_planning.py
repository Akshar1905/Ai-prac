#Q.) Design and implement a classical planning algorithm to solve a goal-based problem such as the block world problem.



# Goal Stack Planning for Block World

# Define actions
def is_clear(block, state):
    for x in state:
        if state[x] == block:
            return False
    return True

def goal_stack_planning(initial_state, goal_state):
    stack = []
    plan = []
    state = initial_state.copy()

    # Push all goal conditions
    for goal in reversed(list(goal_state.items())):
        stack.append(goal)

    while stack:
        top = stack.pop()

        if isinstance(top, tuple):
            if top[0] == "putdown":
                # Execute putdown action
                _, block = top
                state[block] = "table"
                plan.append(f"Put {block} on table")
            elif top[0] == "stack":
                # Execute stack action
                _, block, target = top
                state[block] = target
                plan.append(f"Stack {block} on {target}")
            elif top[0] == "clear":
                # Check precondition
                block = top[1]
                if not is_clear(block, state):
                    # Need to clear it
                    on_top = None
                    for b, pos in state.items():
                        if pos == block:
                            on_top = b
                            break
                    if on_top:
                        stack.append(("putdown", on_top))
                        stack.append(("clear", on_top))
            else:
                # It's a goal
                block, on = top
                if state.get(block) == on:
                    continue
                # Need to achieve this goal
                if on == "table":
                    # Move block to table
                    stack.append(("putdown", block))
                    stack.append(("clear", block))
                else:
                    # Stack block on another block
                    stack.append(("stack", block, on))
                    stack.append(("clear", block))
                    stack.append(("clear", on))

    return plan


# ----------- MAIN PROGRAM -----------

initial_state = {
    'A': 'table',
    'B': 'table',
    'C': 'A'
}

goal_state = {
    'C': 'table',
    'B': 'C',
    'A': 'B'
}

plan = goal_stack_planning(initial_state, goal_state)

print("Plan to reach goal state:")
for step in plan:
    print(step)


###🔹 Aim
To implement Goal Stack Planning for block world problem.
🔹 Theory
Goal Stack Planning is used in AI planning problems.
It uses a stack to store goals and actions required to achieve them.
🔹 Algorithm
Push goal into stack
Check if goal is satisfied
If not → push actions
Execute actions step by step
🔹 Explanation of Code
Initial and goal states are defined
Stack stores actions like “stack” and “putdown”
State updates after each action
Final plan is printed
🔹 Conclusion
It is useful in robotics and automated planning systems.
