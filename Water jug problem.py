from collections import deque
from math import gcd


def generate_next_states(state, jug1_capacity, jug2_capacity):
    """
    Generate all valid states from the current state.

    State format:
        (water_in_jug1, water_in_jug2)
    """

    jug1, jug2 = state
    next_states = []

    # 1. Fill Jug 1 completely
    next_states.append(
        ((jug1_capacity, jug2), "Fill Jug 1")
    )

    # 2. Fill Jug 2 completely
    next_states.append(
        ((jug1, jug2_capacity), "Fill Jug 2")
    )

    # 3. Empty Jug 1
    next_states.append(
        ((0, jug2), "Empty Jug 1")
    )

    # 4. Empty Jug 2
    next_states.append(
        ((jug1, 0), "Empty Jug 2")
    )

    # 5. Pour Jug 1 into Jug 2
    transfer_to_jug2 = min(
        jug1,
        jug2_capacity - jug2
    )

    next_states.append(
        (
            (
                jug1 - transfer_to_jug2,
                jug2 + transfer_to_jug2
            ),
            "Pour Jug 1 into Jug 2"
        )
    )

    # 6. Pour Jug 2 into Jug 1
    transfer_to_jug1 = min(
        jug2,
        jug1_capacity - jug1
    )

    next_states.append(
        (
            (
                jug1 + transfer_to_jug1,
                jug2 - transfer_to_jug1
            ),
            "Pour Jug 2 into Jug 1"
        )
    )

    return next_states


def construct_solution_path(parent, action, goal_state):
    """
    Construct the solution path from the initial state
    to the goal state.
    """

    path = []
    current_state = goal_state

    while current_state is not None:
        path.append(
            (
                current_state,
                action.get(current_state, "Initial State")
            )
        )

        current_state = parent[current_state]

    path.reverse()

    return path


def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    """
    Solve the Water Jug Problem using BFS.
    """

    initial_state = (0, 0)

    queue = deque([initial_state])
    visited = {initial_state}

    parent = {initial_state: None}
    action = {initial_state: "Initial State"}

    explored_order = []

    while queue:
        current_state = queue.popleft()
        explored_order.append(current_state)

        jug1, jug2 = current_state

        if jug1 == target or jug2 == target:
            solution_path = construct_solution_path(
                parent,
                action,
                current_state
            )

            return solution_path, explored_order

        next_states = generate_next_states(
            current_state,
            jug1_capacity,
            jug2_capacity
        )

        for next_state, operation in next_states:
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

                parent[next_state] = current_state
                action[next_state] = operation

    return None, explored_order


def main():
    print("=" * 65)
    print("               WATER JUG PROBLEM")
    print("=" * 65)

    try:
        jug1_capacity = int(
            input("Enter the capacity of Jug 1: ")
        )

        jug2_capacity = int(
            input("Enter the capacity of Jug 2: ")
        )

        target = int(
            input("Enter the target quantity: ")
        )

        if jug1_capacity <= 0 or jug2_capacity <= 0:
            print(
                "Error: Jug capacities must be greater than zero."
            )
            return

        if target < 0:
            print(
                "Error: Target quantity cannot be negative."
            )
            return

        if target == 0:
            print("\nTarget is already achieved.")
            print("Initial state: (0, 0)")
            return

        if target > max(jug1_capacity, jug2_capacity):
            print(
                "\nNo solution exists because the target is "
                "greater than both jug capacities."
            )
            return

        if target % gcd(jug1_capacity, jug2_capacity) != 0:
            print(
                "\nNo solution exists."
            )
            print(
                "Reason: Target is not divisible by the GCD "
                "of the jug capacities."
            )
            return

        solution_path, explored_order = water_jug_bfs(
            jug1_capacity,
            jug2_capacity,
            target
        )

        print("\n" + "=" * 65)
        print("PROBLEM DETAILS")
        print("=" * 65)

        print(f"Jug 1 capacity : {jug1_capacity} litres")
        print(f"Jug 2 capacity : {jug2_capacity} litres")
        print(f"Target quantity: {target} litres")

        print("\n" + "=" * 65)
        print("EXPLORED STATES")
        print("=" * 65)

        for state_number, state in enumerate(
            explored_order,
            start=1
        ):
            print(
                f"State {state_number}: "
                f"Jug 1 = {state[0]}, Jug 2 = {state[1]}"
            )

        print("\n" + "=" * 65)
        print("SOLUTION PATH")
        print("=" * 65)

        if solution_path is None:
            print("No solution exists.")

        else:
            for step_number, path_data in enumerate(
                solution_path
            ):
                state, operation = path_data

                print(
                    f"Step {step_number}: "
                    f"{operation}"
                )

                print(
                    f"        Jug 1 = {state[0]} litres, "
                    f"Jug 2 = {state[1]} litres"
                )

            goal_state = solution_path[-1][0]

            print("\n" + "=" * 65)
            print("FINAL RESULT")
            print("=" * 65)

            print(
                f"Target achieved: {target} litres"
            )

            print(
                f"Final state     : {goal_state}"
            )

            print(
                f"Total operations: "
                f"{len(solution_path) - 1}"
            )

            print(
                f"States explored : "
                f"{len(explored_order)}"
            )

            print(
                "Result          : Solution found"
            )

    except ValueError:
        print(
            "Error: Please enter valid integer values."
        )

    except Exception as error:
        print(
            f"Unexpected error: {error}"
        )


if __name__ == "__main__":
    main()
