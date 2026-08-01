def alpha_beta(
    node_index,
    depth,
    maximizing_player,
    leaf_values,
    max_depth,
    alpha,
    beta,
    trace,
    visited_leaves,
    pruned_leaves
):
  
    if depth == max_depth:
        value = leaf_values[node_index]
        visited_leaves.add(node_index)

        trace.append(
            f"Evaluate Leaf {node_index + 1}: "
            f"value = {value}, alpha = {alpha}, beta = {beta}"
        )

        return value

    if maximizing_player:
        best_value = float("-inf")

        trace.append(
            f"Enter MAX node: depth = {depth}, "
            f"index = {node_index}, "
            f"alpha = {alpha}, beta = {beta}"
        )

        child_indexes = [
            node_index * 2,
            node_index * 2 + 1
        ]

        for child_position, child_index in enumerate(child_indexes):
            value = alpha_beta(
                child_index,
                depth + 1,
                False,
                leaf_values,
                max_depth,
                alpha,
                beta,
                trace,
                visited_leaves,
                pruned_leaves
            )

            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            trace.append(
                f"MAX node updates: best = {best_value}, "
                f"alpha = {alpha}, beta = {beta}"
            )

            if beta <= alpha:
                trace.append(
                    f"PRUNING at MAX node because "
                    f"beta ({beta}) <= alpha ({alpha})"
                )

                remaining_children = child_indexes[
                    child_position + 1:
                ]

                for remaining_child in remaining_children:
                    collect_leaf_indexes(
                        remaining_child,
                        depth + 1,
                        max_depth,
                        pruned_leaves
                    )

                break

        trace.append(
            f"Exit MAX node with value {best_value}"
        )

        return best_value

    else:
        best_value = float("inf")

        trace.append(
            f"Enter MIN node: depth = {depth}, "
            f"index = {node_index}, "
            f"alpha = {alpha}, beta = {beta}"
        )

        child_indexes = [
            node_index * 2,
            node_index * 2 + 1
        ]

        for child_position, child_index in enumerate(child_indexes):
            value = alpha_beta(
                child_index,
                depth + 1,
                True,
                leaf_values,
                max_depth,
                alpha,
                beta,
                trace,
                visited_leaves,
                pruned_leaves
            )

            best_value = min(best_value, value)
            beta = min(beta, best_value)

            trace.append(
                f"MIN node updates: best = {best_value}, "
                f"alpha = {alpha}, beta = {beta}"
            )

            if beta <= alpha:
                trace.append(
                    f"PRUNING at MIN node because "
                    f"beta ({beta}) <= alpha ({alpha})"
                )

                remaining_children = child_indexes[
                    child_position + 1:
                ]

                for remaining_child in remaining_children:
                    collect_leaf_indexes(
                        remaining_child,
                        depth + 1,
                        max_depth,
                        pruned_leaves
                    )

                break

        trace.append(
            f"Exit MIN node with value {best_value}"
        )

        return best_value


def collect_leaf_indexes(
    node_index,
    depth,
    max_depth,
    pruned_leaves
):
    """
    Collect all terminal leaf indexes under a pruned subtree.
    """

    if depth == max_depth:
        pruned_leaves.add(node_index)
        return

    collect_leaf_indexes(
        node_index * 2,
        depth + 1,
        max_depth,
        pruned_leaves
    )

    collect_leaf_indexes(
        node_index * 2 + 1,
        depth + 1,
        max_depth,
        pruned_leaves
    )


def minimax_without_pruning(
    node_index,
    depth,
    maximizing_player,
    leaf_values,
    max_depth
):
    if depth == max_depth:
        return leaf_values[node_index]

    left_value = minimax_without_pruning(
        node_index * 2,
        depth + 1,
        not maximizing_player,
        leaf_values,
        max_depth
    )

    right_value = minimax_without_pruning(
        node_index * 2 + 1,
        depth + 1,
        not maximizing_player,
        leaf_values,
        max_depth
    )

    if maximizing_player:
        return max(left_value, right_value)

    return min(left_value, right_value)


def evaluate_subtree(
    leaf_values,
    start_index,
    subtree_depth,
    maximizing_player
):
    """
    Evaluate a subtree to determine its Minimax value.
    """

    if subtree_depth == 0:
        return leaf_values[start_index]

    left_value = evaluate_subtree(
        leaf_values,
        start_index,
        subtree_depth - 1,
        not maximizing_player
    )

    right_offset = 2 ** (subtree_depth - 1)

    right_value = evaluate_subtree(
        leaf_values,
        start_index + right_offset,
        subtree_depth - 1,
        not maximizing_player
    )

    if maximizing_player:
        return max(left_value, right_value)

    return min(left_value, right_value)


def find_best_first_move(leaf_values, max_depth):

    leaves_per_subtree = len(leaf_values) // 2

    left_value = evaluate_subtree(
        leaf_values,
        0,
        max_depth - 1,
        False
    )

    right_value = evaluate_subtree(
        leaf_values,
        leaves_per_subtree,
        max_depth - 1,
        False
    )

    if left_value > right_value:
        best_move = "Left child"
    elif right_value > left_value:
        best_move = "Right child"
    else:
        best_move = "Either child"

    return best_move, left_value, right_value


def main():
    print("=" * 70)
    print("              ALPHA-BETA PRUNING")
    print("=" * 70)

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
                input(f"Leaf {index + 1}: ")
            )

            leaf_values.append(value)

        trace = []
        visited_leaves = set()
        pruned_leaves = set()

        alpha_beta_value = alpha_beta(
            node_index=0,
            depth=0,
            maximizing_player=True,
            leaf_values=leaf_values,
            max_depth=max_depth,
            alpha=float("-inf"),
            beta=float("inf"),
            trace=trace,
            visited_leaves=visited_leaves,
            pruned_leaves=pruned_leaves
        )

        minimax_value = minimax_without_pruning(
            node_index=0,
            depth=0,
            maximizing_player=True,
            leaf_values=leaf_values,
            max_depth=max_depth
        )

        best_move, left_value, right_value = (
            find_best_first_move(
                leaf_values,
                max_depth
            )
        )

        print("\n" + "=" * 70)
        print("TERMINAL NODE VALUES")
        print("=" * 70)

        for index, value in enumerate(
            leaf_values,
            start=1
        ):
            print(
                f"Leaf {index}: {value}"
            )

        print("\n" + "=" * 70)
        print("ALPHA-BETA EVALUATION TRACE")
        print("=" * 70)

        for step_number, message in enumerate(
            trace,
            start=1
        ):
            print(
                f"Step {step_number}: {message}"
            )

        print("\n" + "=" * 70)
        print("EVALUATED LEAVES")
        print("=" * 70)

        if visited_leaves:
            for leaf_index in sorted(visited_leaves):
                print(
                    f"Leaf {leaf_index + 1}: "
                    f"{leaf_values[leaf_index]}"
                )
        else:
            print("No leaves were evaluated.")

        print("\n" + "=" * 70)
        print("PRUNED LEAVES")
        print("=" * 70)

        if pruned_leaves:
            for leaf_index in sorted(pruned_leaves):
                print(
                    f"Leaf {leaf_index + 1}: "
                    f"{leaf_values[leaf_index]}"
                )
        else:
            print(
                "No leaf nodes were pruned."
            )

        print("\n" + "=" * 70)
        print("FIRST MOVE ANALYSIS")
        print("=" * 70)

        print(
            f"Value of left subtree : {left_value}"
        )

        print(
            f"Value of right subtree: {right_value}"
        )

        print(
            f"Best first move       : {best_move}"
        )

        total_leaves = len(leaf_values)
        evaluated_count = len(visited_leaves)
        pruned_count = len(pruned_leaves)

        print("\n" + "=" * 70)
        print("SEARCH STATISTICS")
        print("=" * 70)

        print(
            f"Total terminal nodes : {total_leaves}"
        )

        print(
            f"Evaluated leaves     : {evaluated_count}"
        )

        print(
            f"Pruned leaves        : {pruned_count}"
        )

        if total_leaves > 0:
            pruning_percentage = (
                pruned_count / total_leaves
            ) * 100

            print(
                f"Pruning percentage   : "
                f"{pruning_percentage:.2f}%"
            )

        print("\n" + "=" * 70)
        print("FINAL RESULT")
        print("=" * 70)

        print(
            f"Alpha-Beta value : {alpha_beta_value}"
        )

        print(
            f"Minimax value    : {minimax_value}"
        )

        print(
            f"Best first move  : {best_move}"
        )

        if alpha_beta_value == minimax_value:
            print(
                "Verification     : Pass"
            )
        else:
            print(
                "Verification     : Fail"
            )

        print(
            "Result           : Search completed"
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
