from itertools import permutations


def word_to_number(word, assignment):
    """
    Convert a word into its numerical value
    using the given letter-to-digit assignment.

    Example:
        SEND with S=9, E=5, N=6, D=7
        becomes 9567.
    """

    number = 0

    for letter in word:
        number = number * 10 + assignment[letter]

    return number


def solve_cryptarithmetic(word1, word2, result):
    """
    Solve a two-word cryptarithmetic addition problem.

    Example:
        SEND + MORE = MONEY

    Returns:
        solutions          : All valid solutions
        assignments_tested : Number of valid assignments checked
    """

    word1 = word1.upper()
    word2 = word2.upper()
    result = result.upper()

    # Preserve the order in which letters appear
    letters = []

    for letter in word1 + word2 + result:
        if letter not in letters:
            letters.append(letter)

    if len(letters) > 10:
        return [], 0, letters

    # Leading letters cannot be assigned zero
    leading_letters = set()

    if len(word1) > 1:
        leading_letters.add(word1[0])

    if len(word2) > 1:
        leading_letters.add(word2[0])

    if len(result) > 1:
        leading_letters.add(result[0])

    solutions = []
    assignments_tested = 0

    for digits in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, digits))

        # A multi-digit number cannot begin with zero
        if any(
            assignment[letter] == 0
            for letter in leading_letters
        ):
            continue

        assignments_tested += 1

        number1 = word_to_number(word1, assignment)
        number2 = word_to_number(word2, assignment)
        result_number = word_to_number(result, assignment)

        if number1 + number2 == result_number:
            solutions.append(
                {
                    "assignment": assignment.copy(),
                    "number1": number1,
                    "number2": number2,
                    "result_number": result_number
                }
            )

    return solutions, assignments_tested, letters


def display_vertical_addition(number1, number2, result_number):
    """
    Display the addition in vertical format.
    """

    width = max(
        len(str(number1)),
        len(str(number2)) + 1,
        len(str(result_number))
    )

    print(str(number1).rjust(width))
    print(("+" + str(number2)).rjust(width))
    print("-" * width)
    print(str(result_number).rjust(width))


def validate_solution(solution):
    """
    Validate that the numerical addition is correct
    and all assigned digits are unique.
    """

    assignment = solution["assignment"]

    digits = list(assignment.values())

    unique_digits = len(digits) == len(set(digits))

    correct_addition = (
        solution["number1"]
        + solution["number2"]
        == solution["result_number"]
    )

    return unique_digits and correct_addition


def main():
    print("=" * 70)
    print("              CRYPTARITHMETIC PROBLEM")
    print("=" * 70)

    word1 = input(
        "Enter the first word: "
    ).strip().upper()

    word2 = input(
        "Enter the second word: "
    ).strip().upper()

    result = input(
        "Enter the result word: "
    ).strip().upper()

    if not word1 or not word2 or not result:
        print(
            "Error: Words cannot be empty."
        )
        return

    if not (
        word1.isalpha()
        and word2.isalpha()
        and result.isalpha()
    ):
        print(
            "Error: Enter alphabetic words only."
        )
        return

    solutions, assignments_tested, letters = (
        solve_cryptarithmetic(
            word1,
            word2,
            result
        )
    )

    print("\n" + "=" * 70)
    print("PROBLEM DETAILS")
    print("=" * 70)

    print(f"First word      : {word1}")
    print(f"Second word     : {word2}")
    print(f"Result word     : {result}")

    print(
        f"Equation        : "
        f"{word1} + {word2} = {result}"
    )

    print(
        f"Unique letters  : "
        f"{', '.join(letters)}"
    )

    print(
        f"Number of letters: {len(letters)}"
    )

    if len(letters) > 10:
        print("\n" + "=" * 70)
        print("FINAL RESULT")
        print("=" * 70)

        print(
            "No solution can exist because there are "
            "more than 10 unique letters."
        )

        return

    print("\n" + "=" * 70)
    print("SEARCH INFORMATION")
    print("=" * 70)

    print(
        f"Assignments tested: {assignments_tested}"
    )

    print(
        f"Solutions found   : {len(solutions)}"
    )

    print("\n" + "=" * 70)
    print("SOLUTIONS")
    print("=" * 70)

    if not solutions:
        print(
            "No valid solution exists."
        )

    else:
        for solution_number, solution in enumerate(
            solutions,
            start=1
        ):
            assignment = solution["assignment"]

            print(
                f"\nSolution {solution_number}"
            )

            print("-" * 40)

            print("Letter assignments:")

            for letter in letters:
                print(
                    f"{letter} = {assignment[letter]}"
                )

            print("\nNumerical equation:")

            print(
                f"{solution['number1']} + "
                f"{solution['number2']} = "
                f"{solution['result_number']}"
            )

            print("\nVertical addition:")

            display_vertical_addition(
                solution["number1"],
                solution["number2"],
                solution["result_number"]
            )

            if validate_solution(solution):
                print(
                    "\nValidation: Pass"
                )
            else:
                print(
                    "\nValidation: Fail"
                )

    print("\n" + "=" * 70)
    print("FINAL RESULT")
    print("=" * 70)

    print(
        f"Puzzle          : "
        f"{word1} + {word2} = {result}"
    )

    print(
        f"Unique letters  : {len(letters)}"
    )

    print(
        f"Solutions found : {len(solutions)}"
    )

    if solutions:
        print(
            "Result          : Puzzle solved successfully"
        )
    else:
        print(
            "Result          : No valid solution found"
        )


if __name__ == "__main__":
    main()
