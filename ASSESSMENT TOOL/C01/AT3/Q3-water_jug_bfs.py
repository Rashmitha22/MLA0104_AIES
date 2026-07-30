from collections import deque

CAPACITY_A = 11
CAPACITY_B = 9
TARGET = 8


def get_next_states(state):
    """Return all valid states reachable from the current state."""
    a, b = state
    next_states = []

    # Fill either jug
    next_states.append(((CAPACITY_A, b), "Fill the 11L jug"))
    next_states.append(((a, CAPACITY_B), "Fill the 9L jug"))

    # Empty either jug
    next_states.append(((0, b), "Empty the 11L jug"))
    next_states.append(((a, 0), "Empty the 9L jug"))

    # Pour from 11L jug to 9L jug
    transfer = min(a, CAPACITY_B - b)
    next_states.append(
        ((a - transfer, b + transfer), "Pour 11L jug into 9L jug")
    )

    # Pour from 9L jug to 11L jug
    transfer = min(b, CAPACITY_A - a)
    next_states.append(
        ((a + transfer, b - transfer), "Pour 9L jug into 11L jug")
    )

    return next_states


def bfs():
    """Find the shortest sequence of operations using BFS."""
    initial_state = (0, 0)
    queue = deque([(initial_state, [])])
    visited = {initial_state}

    while queue:
        current_state, path = queue.popleft()
        a, b = current_state

        if a == TARGET or b == TARGET:
            return path, current_state

        for next_state, operation in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                new_path = path + [(operation, next_state)]
                queue.append((next_state, new_path))

    return None, None


def display_solution():
    path, final_state = bfs()

    print("WATER JUG PUZZLE USING BFS")
    print("-" * 45)
    print("Jug A Capacity : 11 litres")
    print("Jug B Capacity : 9 litres")
    print("Target         : 8 litres")
    print("-" * 45)
    print("Initial State  : (0, 0)")

    if path is None:
        print("No solution found.")
        return

    for step, (operation, state) in enumerate(path, start=1):
        print(f"Step {step}: {operation}")
        print(f"        State = {state}")

    print("-" * 45)
    print(f"Goal reached at state: {final_state}")
    print(f"Number of moves: {len(path)}")


if __name__ == "__main__":
    display_solution()
