def forward_chaining(initial_facts, rules, goal):
    known_facts = set(initial_facts)
    inference_trace = []

    changed = True

    while changed:
        changed = False

        for rule_number, rule in enumerate(rules, start=1):
            premises = rule["premises"]
            conclusion = rule["conclusion"]

            # Fire the rule only when all premises are known
            if premises.issubset(known_facts):

                if conclusion not in known_facts:
                    known_facts.add(conclusion)
                    changed = True

                    inference_trace.append(
                        {
                            "rule": rule_number,
                            "premises": premises,
                            "conclusion": conclusion
                 def is_safe(board, row, column, n):
    """
    Check whether a queen can be safely placed
    at board[row][column].
    """

    # Check the same column in previous rows
    for previous_row in range(row):
        if board[previous_row][column] == 1:
            return False

    # Check upper-left diagonal
    current_row = row - 1
    current_column = column - 1

    while current_row >= 0 and current_column >= 0:
        if board[current_row][current_column] == 1:
            return False

        current_row -= 1
        current_column -= 1

    # Check upper-right diagonal
    current_row = row - 1
    current_column = column + 1

    while current_row >= 0 and current_column < n:
        if board[current_row][current_column] == 1:
            return False

        current_row -= 1
        current_column += 1

    return True


def solve_n_queens(board, row, n, solutions, trace):
    """
    Solve the N-Queen problem using backtracking.
    """

    # All queens have been placed
    if row == n:
        solution = [
            board_row[:]
            for board_row in board
        ]

        solutions.append(solution)

        trace.append(
            f"Solution {len(solutions)} found"
        )

        return

    for column in range(n):
        trace.append(
            f"Trying Queen at Row {row + 1}, "
            f"Column {column + 1}"
        )

        if is_safe(board, row, column, n):
            board[row][column] = 1

            trace.append(
                f"Placed Queen at Row {row + 1}, "
                f"Column {column + 1}"
            )

            solve_n_queens(
                board,
                row + 1,
                n,
                solutions,
                trace
            )

            board[row][column] = 0

            trace.append(
                f"Backtracking from Row {row + 1}, "
                f"Column {column + 1}"
            )

        else:
            trace.append(
                f"Position Row {row + 1}, "
                f"Column {column + 1} is not safe"
            )


def display_board(board):
    """
    Display the chessboard using Q and dots.
    """

    n = len(board)

    print("   " + " ".join(
        str(column + 1)
        for column in range(n)
    ))

    for row_index, row in enumerate(board):
        row_output = []

        for cell in row:
            if cell == 1:
                row_output.append("Q")
            else:
                row_output.append(".")

        print(
            f"{row_index + 1:<2} "
            + " ".join(row_output)
        )


def get_queen_positions(board):
    """
    Return queen positions from a solved board.
    """

    positions = []

    for row_index, row in enumerate(board):
        for column_index, cell in enumerate(row):
            if cell == 1:
                positions.append(
                    (
                        row_index + 1,
                        column_index + 1
                    )
                )

    return positions


def validate_solution(board):
    """
    Validate a completed N-Queen solution.
    """

    n = len(board)
    queen_count = 0

    for row in board:
        queen_count += sum(row)

    if queen_count != n:
        return False

    for row in range(n):
        for column in range(n):
            if board[row][column] == 1:
                board[row][column] = 0

                safe = is_safe(
                    board,
                    row,
                    column,
                    n
                )

                board[row][column] = 1

                if not safe:
                    return False

    return True


def main():
    print("=" * 70)
    print("                    N-QUEEN PROBLEM")
    print("=" * 70)

    try:
        n = int(
            input("Enter the number of queens: ")
        )

        if n <= 0:
            print(
                "Error: Number of queens must be greater than zero."
            )
            return

        board = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]

        solutions = []
        trace = []

        solve_n_queens(
            board,
            0,
            n,
            solutions,
            trace
        )

        print("\n" + "=" * 70)
        print("PROBLEM DETAILS")
        print("=" * 70)

        print(f"Number of queens : {n}")
        print(f"Board size       : {n} × {n}")
        print("Method           : Backtracking")

        print("\n" + "=" * 70)
        print("SEARCH TRACE")
        print("=" * 70)

        if trace:
            for step_number, message in enumerate(
                trace,
                start=1
            ):
                print(
                    f"Step {step_number}: {message}"
                )
        else:
            print("No search steps recorded.")

        print("\n" + "=" * 70)
        print("SOLUTIONS")
        print("=" * 70)

        if not solutions:
            print(
                f"No solution exists for N = {n}."
            )

        else:
            for solution_number, solution in enumerate(
                solutions,
                start=1
            ):
                print(
                    f"\nSolution {solution_number}"
                )

                print("-" * 30)

                display_board(solution)

                positions = get_queen_positions(
                    solution
                )

                formatted_positions = [
                    f"({row}, {column})"
                    for row, column in positions
                ]

                print(
                    "Queen positions: "
                    + ", ".join(formatted_positions)
                )

                if validate_solution(solution):
                    print(
                        "Validation: Pass"
                    )
                else:
                    print(
                        "Validation: Fail"
                    )

        print("\n" + "=" * 70)
        print("FINAL RESULT")
        print("=" * 70)

        print(
            f"Number of queens : {n}"
        )

        print(
            f"Total solutions  : {len(solutions)}"
        )

        print(
            f"Search steps     : {len(trace)}"
        )

        if solutions:
            print(
                "Result           : Solutions found"
            )

            print(
                "Validation       : Pass"
            )
        else:
            print(
                "Result           : No solution exists"
            )

    except ValueError:
        print(
            "Error: Please enter a valid integer."
        )

    except Exception as error:
        print(
            f"Unexpected error: {error}"
        )


if __name__ == "__main__":
    main()       }
                    )

                    # Stop when the goal is derived
                    if conclusion == goal:
                        return (
                            True,
                            known_facts,
                            inference_trace
                        )

    return (
        goal in known_facts,
        known_facts,
        inference_trace
    )


def format_fact(fact):
    """
    Format a fact for display.
    """

    return fact.replace("_", " ").title()


def main():
    print("=" * 70)
    print("                 FORWARD CHAINING")
    print("=" * 70)

    try:
        number_of_facts = int(
            input("Enter the number of initial facts: ")
        )

        if number_of_facts < 0:
            print(
                "Error: Number of facts cannot be negative."
            )
            return

        initial_facts = set()

        print("\nEnter the initial facts:")

        for index in range(number_of_facts):
            fact = input(
                f"Fact {index + 1}: "
            ).strip().lower()

            if not fact:
                print(
                    "Error: Fact cannot be empty."
                )
                return

            initial_facts.add(fact)

        number_of_rules = int(
            input("\nEnter the number of rules: ")
        )

        if number_of_rules < 0:
            print(
                "Error: Number of rules cannot be negative."
            )
            return

        rules = []

        print("\nEnter each rule.")
        print("Enter premises separated by commas.")
        print("Example premises: has_feathers, lays_eggs")
        print("Example conclusion: bird")

        for index in range(number_of_rules):
            print(f"\nRule {index + 1}")

            premise_input = input(
                "Enter premises: "
            ).strip().lower()

            conclusion = input(
                "Enter conclusion: "
            ).strip().lower()

            if not premise_input or not conclusion:
                print(
                    "Error: Premises and conclusion cannot be empty."
                )
                return

            premises = {
                premise.strip()
                for premise in premise_input.split(",")
                if premise.strip()
            }

            if not premises:
                print(
                    "Error: At least one premise is required."
                )
                return

            rules.append(
                {
                    "premises": premises,
                    "conclusion": conclusion
                }
            )

        goal = input(
            "\nEnter the goal to prove: "
        ).strip().lower()

        if not goal:
            print(
                "Error: Goal cannot be empty."
            )
            return

        goal_found, known_facts, inference_trace = (
            forward_chaining(
                initial_facts,
                rules,
                goal
            )
        )

        print("\n" + "=" * 70)
        print("INITIAL FACTS")
        print("=" * 70)

        if initial_facts:
            for fact in sorted(initial_facts):
                print(
                    f"- {format_fact(fact)}"
                )
        else:
            print("No initial facts.")

        print("\n" + "=" * 70)
        print("KNOWLEDGE BASE RULES")
        print("=" * 70)

        if rules:
            for index, rule in enumerate(
                rules,
                start=1
            ):
                premises_text = " AND ".join(
                    format_fact(premise)
                    for premise in sorted(
                        rule["premises"]
                    )
                )

                conclusion_text = format_fact(
                    rule["conclusion"]
                )

                print(
                    f"Rule {index}: "
                    f"IF {premises_text} "
                    f"THEN {conclusion_text}"
                )
        else:
            print("No rules entered.")

        print("\n" + "=" * 70)
        print("INFERENCE TRACE")
        print("=" * 70)

        if inference_trace:
            for step_number, step in enumerate(
                inference_trace,
                start=1
            ):
                premises_text = " AND ".join(
                    format_fact(premise)
                    for premise in sorted(
                        step["premises"]
                    )
                )

                conclusion_text = format_fact(
                    step["conclusion"]
                )

                print(
                    f"Step {step_number}: "
                    f"Rule {step['rule']} fired"
                )

                print(
                    f"    Premises  : {premises_text}"
                )

                print(
                    f"    Conclusion: {conclusion_text}"
                )
        else:
            print(
                "No rule was fired."
            )

        print("\n" + "=" * 70)
        print("ALL KNOWN FACTS")
        print("=" * 70)

        for fact in sorted(known_facts):
            source = (
                "Initial fact"
                if fact in initial_facts
                else "Derived fact"
            )

            print(
                f"- {format_fact(fact)} "
                f"({source})"
            )

        print("\n" + "=" * 70)
        print("GOAL TEST")
        print("=" * 70)

        print(
            f"Goal: {format_fact(goal)}"
        )

        if goal_found:
            print(
                "Goal status: Proved"
            )
        else:
            print(
                "Goal status: Not proved"
            )

        print("\n" + "=" * 70)
        print("FINAL RESULT")
        print("=" * 70)

        print(
            f"Initial facts : {len(initial_facts)}"
        )

        print(
            f"Rules         : {len(rules)}"
        )

        print(
            f"Derived facts : "
            f"{len(known_facts - initial_facts)}"
        )

        print(
            f"Total facts   : {len(known_facts)}"
        )

        print(
            f"Rules fired   : {len(inference_trace)}"
        )

        print(
            f"Goal          : {format_fact(goal)}"
        )

        if goal_found:
            print(
                "Result        : Goal successfully proved"
            )
        else:
            print(
                "Result        : Goal could not be proved"
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
