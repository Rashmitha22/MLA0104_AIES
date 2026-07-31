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
    main()
