from collections import deque

# -----------------------------
# Water Jug Problem Definition
# -----------------------------

JUG1_CAPACITY = 4
JUG2_CAPACITY = 3
GOAL = 2   # Target amount


# Generate next possible states
def get_next_states(state):
    x, y = state
    states = []

    # Fill Jug1
    states.append((JUG1_CAPACITY, y))

    # Fill Jug2
    states.append((x, JUG2_CAPACITY))

    # Empty Jug1
    states.append((0, y))

    # Empty Jug2
    states.append((x, 0))

    # Pour Jug1 -> Jug2
    transfer = min(x, JUG2_CAPACITY - y)
    states.append((x - transfer, y + transfer))

    # Pour Jug2 -> Jug1
    transfer = min(y, JUG1_CAPACITY - x)
    states.append((x + transfer, y - transfer))

    return states


# -----------------------------
# Breadth First Search (BFS)
# -----------------------------
def bfs():
    start = (0, 0)
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        state = path[-1]

        if state in visited:
            continue

        visited.add(state)

        x, y = state
        if x == GOAL or y == GOAL:
            return path

        for next_state in get_next_states(state):
            new_path = list(path)
            new_path.append(next_state)
            queue.append(new_path)

    return None


# -----------------------------
# Depth First Search (DFS)
# -----------------------------
def dfs():
    start = (0, 0)
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        state = path[-1]

        if state in visited:
            continue

        visited.add(state)

        x, y = state
        if x == GOAL or y == GOAL:
            return path

        for next_state in get_next_states(state):
            new_path = list(path)
            new_path.append(next_state)
            stack.append(new_path)

    return None


# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":

    print("---- BFS ----")
    bfs_solution = bfs()
    if bfs_solution:
        for step in bfs_solution:
            print(step)
    else:
        print("No solution found")

    print("\n---- DFS ----")
    dfs_solution = dfs()
    if dfs_solution:
        for step in dfs_solution:
            print(step)
    else:
        print("No solution found")