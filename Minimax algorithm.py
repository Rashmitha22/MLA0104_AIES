def minimax(
    node_index,
    depth,
    maximizing_player,
    leaf_values,
    max_depth,
    trace
):
    """
    Perform Minimax search on a complete binary game tree.

    Parameters:
        node_index        : Current node index
        depth             : Current tree depth
        maximizing_player : True for MAX, False for MIN
        leaf_values       : Utility values of terminal nodes
        max_depth         : Maximum tree depth
        trace             : Stores evaluation details

    Returns:
        Best utility value for the current node
    """

    # Terminal condition
    if depth == max_depth:
        value = leaf_values[node_index]

        trace.append(
            f"Leaf node {node_index} evaluated with value {value}"
        )

        return value

    if maximizing_player:
        best_value = float("-inf")

        trace.append(
            f"MAX node at depth {depth}, index {node_index}"
        )

        # Evaluate left child
        left_value = minimax(
            node_index * 2,
            depth + 1,
            False,
            leaf_values,
            max_depth,
            trace
        )

        # Evaluate right child
        right_value = minimax(
            node_index * 2 + 1,
            depth + 1,
            False,
            leaf_values,
            max_depth,
            trace
        )

        best_value = max(left_value, right_value)

        trace.append(
            f"MAX selects max({left_value}, {right_value}) "
            f"= {best_value}"
        )

        return best_value

    else:
        best_value = float("inf")

        trace.append(
            f"MIN node at depth {depth}, index {node_index}"
        )

        # Evaluate left child
        left_value = minimax(
            node_index * 2,
            depth + 1,
            True,
            leaf_values,
            max_depth,
            trace
        )

        # Evaluate right child
        right_value = minimax(
            node_index * 2 + 1,
            depth + 1,
            True,
            leaf_values,
            max_depth,
            trace
        )

        best_value = min(left_value, right_value)

        trace.append(
            f"MIN selects min({left_value}, {right_value}) "
            f"= {best_value}"
        )

        return best_value


def build_tree_levels(leaf_values, max_depth):
    """
    Build game tree values from bottom to top.
    """

    levels = []
    current_level = leaf_values[:]

    levels.append(current_level)

    maximizing = max_depth % 2 == 0

    while len(current_level) > 1:
        next_level = []

        for index in range(0, len(current_level), 2):
            left = current_level[index]
            right = current_level[index + 1]

            if maximizing:
                next_level.append(max(left, right))
            else:
                next_level.append(min(left, right))

        levels.append(next_level)
        current_level = next_level
        maximizing = not maximizing

    levels.reverse()

    return levels


def find_best_first_move(leaf_values, max_depth):
    """
    Determine whether the first move should be left or right.
    """

    half = len(leaf_values) // 2

    left_subtree = leaf_values[:half]
    right_subtree = leaf_values[half:]

    left_trace = []
    right_trace = []

    left_value = minimax(
        0,
        1,
        False,
        left_subtree,
        max_depth,
        left_trace
    )

    right_value = minimax(
        0,
        1,
        False,
        right_subtree,
        max_depth,
        right_trace
    )

    if left_value > right_value:
        return "Left child", left_value, right_value

    if right_value > left_value:
        return "Right child", left_value, right_value

    return "Either child", left_value, right_value


def main():
    print("=" * 65)
    print("                 MINIMAX ALGORITHM")
    print("=" * 65)

    try:
        max_depth = int(
            input("Enter the depth of the game tree: ")
        )

        if max_depth <= 0:
            print(
                "Error: Tree depth must be greater than zero."
            )
            return

        number_of_leaves = 2 ** max_depth

        print(
            f"\nA complete binary tree of depth {max_depth} "
            f"requires {number_of_leaves} leaf values."
        )

        leaf_values = []

        print("\nEnter utility values of terminal nodes:")

        for index in range(number_of_leaves):
            value = int(
                input(
                    f"Leaf {index + 1}: "
                )
            )

            leaf_values.append(value)

        trace = []

        optimal_value = minimax(
            0,
            0,
            True,
            leaf_values,
            max_depth,
            trace
        )

        levels = build_tree_levels(
            leaf_values,
            max_depth
        )

        print("\n" + "=" * 65)
        print("LEAF NODE VALUES")
        print("=" * 65)

        print(
            " ".join(
                str(value)
                for value in leaf_values
            )
        )

        print("\n" + "=" * 65)
        print("GAME TREE VALUES")
        print("=" * 65)

        for level_number, level in enumerate(levels):
            player = (
                "MAX"
                if level_number % 2 == 0
                else "MIN"
            )

            if level_number == max_depth:
                player = "TERMINAL"

            print(
                f"Level {level_number} "
                f"({player}): {level}"
            )

        print("\n" + "=" * 65)
        print("MINIMAX EVALUATION TRACE")
        print("=" * 65)

        for step_number, message in enumerate(
            trace,
            start=1
        ):
            print(
                f"Step {step_number}: {message}"
            )

        best_move, left_value, right_value = (
            find_best_first_move(
                leaf_values,
                max_depth
            )
        )

        print("\n" + "=" * 65)
        print("FIRST MOVE ANALYSIS")
        print("=" * 65)

        print(
            f"Value of left subtree : {left_value}"
        )

        print(
            f"Value of right subtree: {right_value}"
        )

        print(
            f"Best first move       : {best_move}"
        )

        print("\n" + "=" * 65)
        print("FINAL RESULT")
        print("=" * 65)

        print(
            f"Tree depth       : {max_depth}"
        )

        print(
            f"Terminal nodes   : {number_of_leaves}"
        )

        print(
            f"Optimal value    : {optimal_value}"
        )

        print(
            f"Best first move  : {best_move}"
        )

        print(
            "Starting player  : MAX"
        )

        print(
            "Opponent player  : MIN"
        )

        print(
            "Result           : Minimax evaluation completed"
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
